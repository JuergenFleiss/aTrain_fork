import Foundation
import Metal

// An empty device list is the only unavailable result. A failure after finding
// a device is an execution failure, including compilation or command errors.
let devices = MTLCopyAllDevices()
var result: [String: Any] = [
    "status": "failed",
    "devices": devices.map { device in
        [
            "name": device.name,
            "registry_id": String(device.registryID),
            "low_power": device.isLowPower,
            "removable": device.isRemovable,
            "unified_memory": device.hasUnifiedMemory,
            "max_buffer_length": device.maxBufferLength,
            "recommended_max_working_set_size": device.recommendedMaxWorkingSetSize,
            "max_threads_per_threadgroup": [device.maxThreadsPerThreadgroup.width,
                                           device.maxThreadsPerThreadgroup.height,
                                           device.maxThreadsPerThreadgroup.depth],
            "apple_family_1": device.supportsFamily(.apple1),
            "mac_family_2": device.supportsFamily(.mac2)
        ] as [String: Any]
    }
]

func finish(_ code: Int32) -> Never {
    let data = try! JSONSerialization.data(withJSONObject: result, options: [.prettyPrinted, .sortedKeys])
    print(String(data: data, encoding: .utf8)!)
    exit(code)
}

guard let device = MTLCreateSystemDefaultDevice() else {
    result["status"] = devices.isEmpty ? "unavailable" : "failed"
    result["reason"] = "MTLCreateSystemDefaultDevice returned nil"
    finish(devices.isEmpty ? 77 : 1)
}

do {
    let source = """
    #include <metal_stdlib>
    using namespace metal;
    kernel void double_values(device float *values [[buffer(0)]], uint i [[thread_position_in_grid]]) {
        values[i] *= 2.0f;
    }
    """
    let library = try device.makeLibrary(source: source, options: nil)
    guard let function = library.makeFunction(name: "double_values"),
          let queue = device.makeCommandQueue(),
          let command = queue.makeCommandBuffer(),
          let encoder = command.makeComputeCommandEncoder(),
          let buffer = device.makeBuffer(length: 256 * MemoryLayout<Float>.stride, options: .storageModeShared)
    else { throw NSError(domain: "MetalProbe", code: 1, userInfo: [NSLocalizedDescriptionKey: "resource creation failed"]) }
    let pipeline = try device.makeComputePipelineState(function: function)
    let values = buffer.contents().bindMemory(to: Float.self, capacity: 256)
    for i in 0..<256 { values[i] = Float(i) }
    encoder.setComputePipelineState(pipeline)
    encoder.setBuffer(buffer, offset: 0, index: 0)
    encoder.dispatchThreads(MTLSize(width: 256, height: 1, depth: 1),
                            threadsPerThreadgroup: MTLSize(width: min(256, pipeline.maxTotalThreadsPerThreadgroup), height: 1, depth: 1))
    encoder.endEncoding()
    command.commit()
    command.waitUntilCompleted()
    guard command.status == .completed else {
        throw command.error ?? NSError(domain: "MetalProbe", code: 2, userInfo: [NSLocalizedDescriptionKey: "command did not complete"])
    }
    guard (0..<256).allSatisfy({ values[$0] == Float($0 * 2) }) else {
        throw NSError(domain: "MetalProbe", code: 3, userInfo: [NSLocalizedDescriptionKey: "incorrect compute result"])
    }
    result["status"] = "passed"
    result["selected_device"] = device.name
    result["verified_elements"] = 256
    result["gpu_seconds"] = command.gpuEndTime - command.gpuStartTime
    finish(0)
} catch {
    result["reason"] = String(describing: error)
    finish(1)
}
