print("conversions available:km to m,m to km,km to miles")
conversion=["km to m",
      "m to km",
      "km to miles"]
convert=str(input("enter the conversion you need in the unit of length"))
if convert== conversion[0] or convert=="kilometre to metre" :
  x=float(input("enter value of distance in km"))
  print(x,"km = ",1000*x," m")
elif convert== conversion[1] or convert=="metre to kilometre" :
  y=float(input("enter value of distance in m"))
  print(y,"m = ",0.001*y," km")
elif convert== conversion[2] or convert=="kilometre to mile" :
  z=float(input("enter value of distance in km"))
  print(z,"km = ",z/1.609," miles")
