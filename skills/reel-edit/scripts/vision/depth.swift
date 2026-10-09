import Foundation
import CoreML
import Vision
import CoreImage
import ImageIO
import UniformTypeIdentifiers
// usage: depth <model.mlpackage|.mlmodelc> <inDir> <outDir> [step]   or  depth <model> --info
let a=CommandLine.arguments
var murl=URL(fileURLWithPath: a[1])
if murl.pathExtension=="mlpackage" { let c=URL(fileURLWithPath: a[1].replacingOccurrences(of: ".mlpackage", with: ".mlmodelc")); if !FileManager.default.fileExists(atPath: c.path) { let tmp=try MLModel.compileModel(at: murl); try? FileManager.default.removeItem(at: c); try FileManager.default.moveItem(at: tmp, to: c) }; murl=c }
let cfg=MLModelConfiguration(); cfg.computeUnits = .all
let ml=try MLModel(contentsOf: murl, configuration: cfg)
if a[2]=="--info" { print(ml.modelDescription.inputDescriptionsByName); print(ml.modelDescription.outputDescriptionsByName); exit(0) }
let inDir=a[2], outDir=a[3]; let step=a.count>4 ? Int(a[4])! : 1
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)
let vm=try VNCoreMLModel(for: ml); let ctx=CIContext()
let files=try FileManager.default.contentsOfDirectory(atPath: inDir).filter{$0.hasSuffix(".jpg")}.sorted()
var n=0
for (i,f) in files.enumerated() where i % step == 0 {
  let s=CGImageSourceCreateWithURL(URL(fileURLWithPath: inDir+"/"+f) as CFURL,nil)!; let cg=CGImageSourceCreateImageAtIndex(s,0,nil)!
  let req=VNCoreMLRequest(model: vm); req.imageCropAndScaleOption = .scaleFill
  try VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
  var ci:CIImage?
  if let r=req.results?.first as? VNPixelBufferObservation { ci=CIImage(cvPixelBuffer: r.pixelBuffer) }
  else if let r=req.results?.first as? VNCoreMLFeatureValueObservation, let arr=r.featureValue.multiArrayValue { print("multiarray",arr.shape); exit(1) }
  guard var img=ci else { print("no result"); continue }
  img=img.transformed(by: CGAffineTransform(scaleX: CGFloat(cg.width/2)/img.extent.width, y: CGFloat(cg.height/2)/img.extent.height))
  let out=URL(fileURLWithPath: outDir+"/"+f.replacingOccurrences(of: ".jpg", with: ".png"))
  if let o=ctx.createCGImage(img, from: img.extent, format: .L16, colorSpace: CGColorSpaceCreateDeviceGray()), let d=CGImageDestinationCreateWithURL(out as CFURL, UTType.png.identifier as CFString, 1, nil) { CGImageDestinationAddImage(d,o,nil); CGImageDestinationFinalize(d); n+=1 }
}
print("depth",n)
