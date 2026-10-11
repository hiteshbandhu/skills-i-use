import Foundation
import Vision
import CoreImage
import ImageIO
// usage: flow <inDir> <outDir> [maxFrames]  -> raw float32 (H,W,2) flow from frame i to i+1, at 270x480
let a=CommandLine.arguments; let inDir=a[1], outDir=a[2]; let maxN=a.count>3 ? Int(a[3])! : 100000
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
let ctx=CIContext()
func load(_ f:String)->CGImage{ let s=CGImageSourceCreateWithURL(URL(fileURLWithPath: inDir+"/"+f) as CFURL,nil)!; let im=CIImage(cgImage: CGImageSourceCreateImageAtIndex(s,0,nil)!).transformed(by: CGAffineTransform(scaleX: 0.25, y: 0.25)); return ctx.createCGImage(im, from: im.extent)! }
var n=0
for i in 0..<min(files.count-1,maxN) {
  let A=load(files[i]), B=load(files[i+1])
  let req=VNGenerateOpticalFlowRequest(targetedCGImage: B, options: [:]); req.computationAccuracy = .medium; req.outputPixelFormat = kCVPixelFormatType_TwoComponent32Float
  let h=VNImageRequestHandler(cgImage: A, options: [:])
  do { try h.perform([req]) } catch { print("err",error); continue }
  guard let pb=req.results?.first?.pixelBuffer else { continue }
  CVPixelBufferLockBaseAddress(pb,.readOnly)
  let w=CVPixelBufferGetWidth(pb), hh=CVPixelBufferGetHeight(pb), bpr=CVPixelBufferGetBytesPerRow(pb)
  var data=Data(capacity: w*hh*8); let base=CVPixelBufferGetBaseAddress(pb)!
  for y in 0..<hh { data.append(Data(bytes: base.advanced(by: y*bpr), count: w*8)) }
  CVPixelBufferUnlockBaseAddress(pb,.readOnly)
  try data.write(to: URL(fileURLWithPath: outDir+"/"+String(format:"%04d_%dx%d.f32",i,w,hh))); n+=1
}
print("flow",n)
