print("PRODUCTO INTEGRADOR DE APRENDIZAJE - PIA CONTABILIDAD - PRESUPUESTO MAESTRO")
#1erSem
unidades=int(input("Dime las unidades por vender del primer semestre: "))
precio_venta=int(input("Dime el precio de venta: "))
multiplicacion=unidades*precio_venta
print("la suma es", multiplicacion)
#2doSem
unidades2=int(input("Dime las unidades a vender del segundo semestre: "))
precio_venta2=int(input("Dime el precio de venta: "))
multiplicacion1=unidades2*precio_venta2
print("la suma es", multiplicacion1)
#Importe venta 1er y 2do sem
print("La suma total del Importe de venta del primer semestre, y del segundo semestre son: ", multiplicacion+multiplicacion1 )
print("**********************************")
#MATERIAL CE
unidades3=int(input("Dime las unidades a vender del primer semestre del producto 'DI': "))
precio_venta3=int(input("Dime el precio de venta: "))
multiplicacion2=unidades3*precio_venta3
print("la suma es", multiplicacion2)
#2doSem
unidades4=int(input("Dime las unidades a vender del segundo semestre del producto 'DI': "))
precio_venta4=int(input("Dime el precio de venta: "))
multiplicacion3=unidades4*precio_venta4
print("la suma es", multiplicacion3)
#Importe venta 1er y 2do sem
print("La suma total del Importe de venta del primer semestre, y del segundosemestre son: ", multiplicacion2+multiplicacion3)
print("**********************************")
#MATERIAL CR
unidades4=int(input("Dime las unidades a vender del primer semestre: "))
precio_venta4=int(input("Dime el precio de venta: "))
multiplicacion4=unidades4*precio_venta4
print("la suma es", multiplicacion4)
#Segundo semestre
unidades5=int(input("Dime las unidades a vender del segundo semestre: "))
precio_venta5=int(input("Dime el precio de venta: "))
multiplicacion5=unidades5*precio_venta5
print("la suma es", multiplicacion5)
#Importe venta 1er y 2do sem
print("La suma total del Importe de venta del primer y segundo semestre son: ", multiplicacion4+multiplicacion5)
print("**********************************")
suma= (multiplicacion+multiplicacion2+multiplicacion4)
suma2=(multiplicacion1+multiplicacion3+multiplicacion5)
sumatotal=(suma+suma2)
print("El total de ventas en el primer semestre fueron", suma )
print("El total de ventas en el segundo semestre fueron", suma2 )
print("El total de ventas en los 2 semestre fue de", sumatotal)
print("**********************************")
print("**********************************")
#Determinacion del saldo de clientes y flujo de entradas
print ("SALDO DE CLIENTES Y FLUJO DE ENTRADAS")
SaldoClientes=int(input( " Cual es el saldo de clientes del 31-Dic-2015: " ))
TotalClientes2016=SaldoClientes+sumatotal
print(" Su total de clientes de 2016 fue : " , TotalClientes2016 )
print("**********************************")
#Entradas de Efectivo
Cobranza2015=float(input( " Cual es la Cobranza del 2015 "))
Cobranza2016=float(input( " Cual es la Cobranza del 2016 "))
Cobranza2016 = sumatotal * 0.9
TotalEntradas2016=int(input(" Cual es el Total de Entradas Del 2016 "))
TotalEntradas2016= Cobranza2015 + Cobranza2016
print("**********************************")
SaldoClientes2016 = TotalClientes2016 - TotalEntradas2016
print(" Su Saldo de Clientes del 2016 : " , SaldoClientes2016)
print("**********************************")
#3.Presupuesto de Produccion
print("PRESUPUESTO DE PRODUCCION")
#CL Unidades Vender
print( " PRODUCTO D " )
unidadesavendercl1=multiplicacion
unidadesavendercl2=multiplicacion1
print("unidades a vender en 1 semestre son: " , unidades)
print("unidades a vender en 2 semestre son: " , unidades2)
unidadesavenderclTotal15=unidades + unidades2
print("unidades totales a vender son" , unidadesavenderclTotal15)
#CL Inventario final
inventariofinalcl1=int(input("Ingresa la cifra que genero en el inventario final del 1 semestre"))
print("el inventario final del 1 semestre es",inventariofinalcl1)
inventariofinalcl2=int(input("Ingresa la cifra que genero en el inventario final del 2 semestre"))
print("el inventario final del 2 semestre es",inventariofinalcl2)
inventariofinalclTotal2015=inventariofinalcl2
print("el inventario final es",inventariofinalclTotal2015)
#CL Total de Unidades
totalunidadesD= unidades + 10000
totalunidadesD2= unidades2 + 7000 
totalunidadescl1=unidades + inventariofinalcl1
print( "El Total de Unidades en el 1 Semestre son :" , totalunidadesD)
totalunidadescl2=unidades + inventariofinalcl2
print( "El Total de Unidades en el 2 Semestre son :" , totalunidadesD2)
totalunidadesclTotal2015=unidadesavenderclTotal15 + inventariofinalclTotal2015
print( "El Total de Unidades son :" , totalunidadesclTotal2015)
#CL Inventario Inicial
inventarioinicialcl1=int(input("Ingresa el inventario inicial del 1er semestre: " ))
print("El inventario inicial del 1 semestre es: ", inventarioinicialcl1)
inventarioinicialcl2=inventariofinalcl1
print("El inventario inicial del 2 semestre es: ", inventarioinicialcl2)
inventarioinicialclTotal2015=inventarioinicialcl1
print("El inventario inicial total son ", inventarioinicialclTotal2015)
#CL Unidades a Producir
unidadesaproducircl1=totalunidadescl1-inventarioinicialcl1
print("unidades a producir en 1 semestre son: " , unidadesaproducircl1)
unidadesaproducircl2=totalunidadescl2-inventarioinicialcl2
print("unidades a producir en 2 semestre son: " , unidadesaproducircl2)
unidadesaproducirclTotal2015=totalunidadesclTotal2015-inventarioinicialclTotal2015
print("unidades a producir son: " , unidadesaproducirclTotal2015)
#Ce Unidades Vender
print(" PRODUCTO DI " )
unidades44= 4000
unidadesavenderce1=unidades3
unidadesavenderce2=unidades44
print("unidades a vender en 1 semestre son: " , unidadesavenderce1)
print("unidades a vender en 2 semestre son: " , unidadesavenderce2)
unidadesavenderceTotal15=unidadesavenderce1 + unidadesavenderce2
print("unidades totales a vender son: " , unidadesavenderceTotal15)
#CL Inventario final
inventariofinalce1=int(input("Ingresa la cifra que genero en el inventario final del 1 semestre: "))
print("el inventario final del 1 semestre es: ",inventariofinalce1)
inventariofinalce2=int(input("Ingresa la cifra que genero en el inventario final del 2semestre: "))
print("el inventario final del 2 semestre es: ",inventariofinalce2)
inventariofinalceTotal2015=inventariofinalce2
print("el inventario final es: ",inventariofinalceTotal2015)
#CL Total de Unidades
totalunidadesce1=unidadesavenderce1 + inventariofinalce1
print( "El Total de Unidades en el 1 Semestre son :" , totalunidadesce1)
totalunidadesce2=unidadesavenderce2 + inventariofinalce2
print( "El Total de Unidades en el 2 Semestre son :" , totalunidadesce2)
totalunidadesceTotal2015=unidadesavenderceTotal15+inventariofinalceTotal2015
print( "El Total de Unidades son :" , totalunidadesceTotal2015)
#CL Inventario Inicial
inventarioinicialce1=int(input("Ingresa el inventario inicial del 1er semestre: " ))
print("El inventario inicial del 1 semestre es: ", inventarioinicialce1)
inventarioinicialce2=inventariofinalce1
print("El inventario inicial del 2 semestre es: ", inventarioinicialce2)
inventarioinicialceTotal2015=inventarioinicialce1
print("El inventario inicial total son: ", inventarioinicialceTotal2015)
#CE Unidades a Producir
unidadesaproducirce1=totalunidadesce1-inventarioinicialce1
print("unidades a producir en 1 semestre son: " , unidadesaproducirce1)
unidadesaproducirce2=totalunidadesce2-inventarioinicialce2
print("unidades a producir en 2 semestre son: " , unidadesaproducirce2)
unidadesaproducirceTotal2015=totalunidadesceTotal2015-inventarioinicialceTotal2015
print("unidades a producir son: " , unidadesaproducirceTotal2015)
#Ce Unidades Vender
print(" PRODUCTO Z " )
unidsz=5000
unidsz2=5000
unidadesavendercr1=unidsz
unidadesavendercr2=unidsz2
print("unidades a vender en 1 semestre son: " , unidadesavendercr1)
print("unidades a vender en 2 semestre son: " , unidadesavendercr2)
unidadesavendercrTotal15=unidadesavendercr1 + unidadesavendercr2
print("unidades totales a vender son: " , unidadesavendercrTotal15)
#CL Inventario final
inventariofinalcr1=int(input("Ingresa la cifra que genero en el inventario final del 1 semestre: "))
print("el inventario final del 1 semestre es: ",inventariofinalcr1)
inventariofinalcr2=int(input("Ingresa la cifra que genero en el inventario final del 2 semestre: "))
print("el inventario final del 2 semestre es: ",inventariofinalcr2)
inventariofinalcrTotal2015=inventariofinalcr2
print("el inventario final es: ",inventariofinalcrTotal2015)
#CL Total de Unidades
totalunidadescr1=unidadesavendercr1 + inventariofinalcr1
print( "El Total de Unidades en el 1 Semestre son :" , totalunidadescr1)
totalunidadescr2=unidadesavendercr2 + inventariofinalcr2
print( "El Total de Unidades en el 2 Semestre son :" , totalunidadescr2)
totalunidadescrTotal2015=unidadesavendercrTotal15 + inventariofinalcrTotal2015
print( "El Total de Unidades son :" , totalunidadescrTotal2015)
#CL Inventario Inicial
inventarioinicialcr1=int(input("Ingresa el inventario inicial del 1er semestre: " ))
print("El inventario inicial del 1 semestre es: ", inventarioinicialcr1)
inventarioinicialcr2=inventariofinalcr1
print("El inventario inicial del 2 semestre es: ", inventarioinicialcr2)
inventarioinicialcrTotal2015=inventarioinicialcr1
print("El inventario inicial total son: ", inventarioinicialcrTotal2015)
#CR Unidades a Producir
unidadesaproducircr1=totalunidadescr1-inventarioinicialcr1
print("unidades a producir en 1 semestre son: " , unidadesaproducircr1)
unidadesaproducircr2=totalunidadescr2-inventarioinicialcr2
print("unidades a producir en 2 semestre son: " , unidadesaproducircr2)
unidadesaproducircrTotal2015=totalunidadescrTotal2015-inventarioinicialcrTotal2015
print("unidades a producir son: " , unidadesaproducircrTotal2015)
#4
print("PRESUPUESTO DE REQUERIMIENTO DE MATERIALES")
totalmaterialCL= unidades
print("Total Unidades D a Producir 2015 son: ", totalmaterialCL)
#CL 1ER SEMESTRE
#AQUI VA EL TOTAL DE MATERIAL A PRODUCIR
materialA=int(input("Cuanto material A requieres para el primer semestre? "))
mat=(unidades * materialA)
print("El total de material A requerido es: ", mat)
print("Total Material A, a Producir 2015 son ", totalmaterialCL)
#CL 2DO SEMESTRE
mat1=(materialA*2000)
print("El total de material A del segundo semestre requerido es: ", mat1)
totalA=(mat1+mat)
print("El total de Material Requerido para el 2015 es",totalA)
print("**********")
#CL MATERIAL B 1ER SEMESTRE
materialB=int(input("Cuanto material B requieres para el primer semestre? "))
materi=(materialB*unidades)
print("El total de material B requerido es: ", materi)
#CL MATERIAL B 2DO SEMESTRE
mat11=(materialB*2000)
TotalB=(materi+mat1)
print("El total de material B del segundo semestre requerido es: ", mat11)
total1b2=(60000+12000)
print("Total Unidades Material B a Producir 2015 son",total1b2)
print("**********")
#MATERIAL C 1ER SEMESTRE
materialC=int(input("Cuanto material C requieres para el primer semestre? "))
materic=(materialC*unidades)
print("El total de material C requerido es: ", materic)
#MATERIAL C 2DO SEMESTRE
mater=(materialC*2000)
TotalC=(90000+18000)
print("El total de material A del segundo semestre requerido es: ", mater)
print("Total Unidades Material C a Producir 2015 son", TotalC)
print("**********")
#CE
totalmaterialCE= (unidadesaproducirce1 + unidadesaproducirce2)
unidadesDIprod=6000
print("Total Unidades DI a Producir 2015 son", unidadesDIprod)
print("***************************************")
#CE 1ER SEMESTRE
#AQUI VA EL TOTAL DE MATERIAL A PRODUCIR
materialCE=int(input("Cuanto material A requieres para el primer semestre? "))
totalmateprod=(6000*13)
mate=(materialCE* 6000)
print("El total de material A requerido es: ", mate)
#CR 2DO SEMESTRE
mate1=(materialCE*2000)
print("El total de material A del segundo semestre requerido es: ", mate1)
total12=(mate+mate1)
print("El total de Material A Requerido para el 2015 es",total12)
print("**********")
#CR MATERIAL B 21ER SEMESTRE
materialCEB=int(input("Cuanto material B requieres para el primer semestre? "))
materCE=(materialCEB*6000)
print("El total de material B requerido es: ", materCE)
#CR MATERIAL B 2DO SEMESTRE
materialCEC=(materialCEB*2000)
TotalCC=(materCE+materialCEC)
print("El total de material B del segundo semestre requerido es: ", materialCEC)
print("Total Unidades Material B a Producir 2015 son",TotalCC)
print("**********")
#CE
#MATERIAL C 1ER SEMESTRE
materialCC=int(input("Cuanto material C requieres para el primer semestre? "))
matericc=(materialCC*6000)
print("El total de material C requerido es: ", matericc)
#MATERIAL C 2DO SEMESTRE
matt=(materialCC*2000)
TotalCCC=(matericc+matt)
print("El total de material C del segundo semestre requerido es: ", matt)
print("Total Unidades Material C a Producir 2015 son", TotalCCC)
print("**********")
#PRODUCTO Z 1ER SEMESTRE
materialCR=int(input("Cuanto material A requieres para el primer semestre? "))
mateCRR=(materialCR* 5000)
print("El total de material A requerido es: ", mateCRR)
#CR 2DO SEMESTRE
materialCR5=int(input("Cuanto material A requieres para el segundo semestre? "))
materiales1=(materialCR5*2000)
print("El total de material A del segundo semestre requerido es: ", materiales1)
totalCR1=(mateCRR+materiales1)
print("El total de Material Requerido para el 2015 es",totalCR1)
print("**********")
#CR MATERIAL B PRIMER SEMESTRE
materialCRB=int(input("Cuanto material B requieres para el primer semestre? "))
materCR=(materialCRB*5000)
print("El total de material B requerido es: ", materCR)
#CR MATERIAL B 2DO SEMESTRE
materialCCR=(materialCRB*2000)
TotalCC=(materCR+materialCCR)
print("El total de material B del segundo semestre requerido es: ", materialCCR)
print("Total Unidades Material B a Producir 2015 son",TotalCC)
print("**********")
#PRODUCTO Z
#MATERIAL C 1ER SEMESTRE
materialCC3=int(input("Cuanto material C requieres para el primer semestre? "))
matericcr=(materialCC3*5000)
print("El total de material C requerido es: ", matericcr)
#MATERIAL C 2DO SEMESTRE
matter=(materialCC3*2000)
TotalC4=(matericcr+matter)
print("El total de material C del segundo semestre requerido es: ", matter)
print("Total Unidades Material C a Producir 2015 son", TotalC4)
print("**********")
#PRIMER SEMESTRE
SumaTotalA=278000
SumaTotalB=132000
SumaTotalC=139000
print("La suma Total de Materiales A en el primer semestre fueron de: ",
SumaTotalA)
print("La suma Total de Materiales B en el primer semestre fueron de: ",
SumaTotalB)
print("La suma Total de Materiales C en el primer semestre fueron de: ",
SumaTotalC)
#SEGUNDO SEMESTRE
SumaTotalAA=76000
SumaTotalBB=38000
SumaTotalCC=36000
print("La suma Total de Materiales A en el segundo semestre fueron de: ",
SumaTotalAA)
print("La suma Total de Materiales B en el segundo semestre fueron de: ",
SumaTotalBB)
print("La suma Total de Materiales C en el segundo semestre fueron de: ",
SumaTotalCC)
#TOTAL SEMESTRES A, B, C
SumaA=(SumaTotalA+SumaTotalAA)
SumaB=(SumaTotalB+SumaTotalBB)
SumaB1=38000
SumaC=(SumaTotalC+SumaTotalCC)
print("La suma Total de Materiales A en todos los semestres fue de: ", SumaA)
print("La suma Total de Materiales B en todos los semestres fue de: ", SumaB)
print("La suma Total de Materiales C en todos los semestres fue de: ", SumaC)
#5 Presupuesto de Compra de Materiales
print("PRESUPUESTO DE COMPRA DE MATERIALES")
#Material A
print( " Material A " )
RequeriMaterialesA=SumaTotalA
RequeriMaterialesA1=SumaTotalAA
print("Los Requerimientos de Materiales en el 1er semestre son" ,
RequeriMaterialesA)
requersmat=76000
print("Los Requerimientos de Materiales en el 2do semestre son" ,
requersmat)
reqmat=RequeriMaterialesA+requersmat
print("Los Requerimientos totales son" , reqmat)
#Material A Inventario final
inventariofinalMA=int(input("Ingresa la cifra que genero en el inventario final del 1er semestre "))
print("El inventario final del 1 semestre es",inventariofinalMA)
inventariofinalMA1=int(input("Ingresa la cifra que genero en el inventario final del 2do semestre "))
print("El inventario final del 2 semestre es",inventariofinalMA1)
inventariofinalMATotal2016=inventariofinalMA1
print("El inventario final total es",inventariofinalMATotal2016)
#Material A Total de Materiales
TotalMateA=RequeriMaterialesA+inventariofinalMA
print("El Total de Materiales de 1er semestre es",TotalMateA)
TotalMateA1=RequeriMaterialesA1+inventariofinalMA1
print("El Total de Materiales de 2do semestre es",TotalMateA1)
TotalMateA2016=TotalMateA+TotalMateA1
print("El Total de Materiales es",TotalMateA2016)
#Material A Inventario Inicial
inventarioInicialMA=int(input("Ingresa la cifra que genero en el inventario inicial del 1er semestre: "))
print("El inventario inicial del 1 semestre es",inventarioInicialMA)
inventarioInicialMA1=int(input("Ingresa la cifra que genero en el inventario inicial del 2do semestre: "))
print("El inventario inicial del 2 semestre es",inventarioInicialMA1)
inventarioInicialMATotal2016=inventariofinalMA
print("El inventario inicial total es",inventarioInicialMATotal2016)
#Material A Material a Comprar
MateComA=SumaTotalA+10000
print("El Total de Materiales a comprar de 1er semestre es",MateComA)
MateComA1=requersmat+8000
print("El Total de Materiales a comprar de 2do semestre es",MateComA1)
TotalCompA2016=MateComA+MateComA1
print("El Total de MaterialesA a Comprar es",TotalMateA2016)
#Material A Precio de Compra
PrecioCompA=int(input("Cual sera el precio de compra del 1er semestre del Material A: "))
PrecioCompA1=int(input("Cual sera el precio de compra del 2do semestre del Material A: "))
#Material A Total de Material en $
TotalmaterialMA=MateComA*PrecioCompA
print("El Total de Material A en dinero de 1er semestre es",TotalmaterialMA)
TotalmaterialMA1=MateComA1*PrecioCompA1
print("El Total de Material A en dinero de 2do semestre es",TotalmaterialMA1)
TotalmaterialMA2016=TotalmaterialMA+TotalmaterialMA1
print("El Total de MaterialesA en dinero es",TotalmaterialMA2016)
#Material B
print( " Material B " )
RequeriMaterialesB=SumaTotalB
RequeriMaterialesB1=SumaTotalBB
print("Los Requerimientos de Materiales en el 1er semestre son" ,
RequeriMaterialesB)
print("Los Requerimientos de Materiales en el 2do semestre son" ,
RequeriMaterialesB1)
print("Los Requerimientos totales son" , SumaB1)
#Material B Inventario final
inventariofinalMB=int(input("Ingresa la cifra que genero en el inventario final del 1er semestre: "))
print("El inventario final del 1 semestre es",inventariofinalMB)
inventariofinalMB1=int(input("Ingresa la cifra que genero en el inventario final del 2do semestre: "))
print("El inventario final del 2 semestre es",inventariofinalMB1)
inventariofinalMBTotal2016=inventariofinalMB1
print("El inventario final total es",inventariofinalMBTotal2016)
#Material B Total de Materiales
TotalMateB=RequeriMaterialesB+inventariofinalMB
print("El Total de Materiales de 1er semestre es",TotalMateB)
TotalMateB1=RequeriMaterialesB1+inventariofinalMB1
print("El Total de Materiales de 2do semestre es",TotalMateB1)
TotalMateB2016=SumaB+inventariofinalMBTotal2016
print("El Total de Materiales es",TotalMateB2016)
#Material B Inventario Inicial
inventarioInicialMB=int(input("Ingresa la cifra que genero en el inventario inicial del 1er semestre: "))
print("El inventario inicial del 1 semestre es",inventarioInicialMB)
inventarioInicialMB1=int(input("Ingresa la cifra que genero en el inventario inicial del 2do semestre: "))
print("El inventario inicial del 2 semestre es",inventarioInicialMB1)
inventarioInicialMBTotal2016=inventariofinalMB
print("El inventario inicial total es",inventarioInicialMBTotal2016)
#Material B Material a Comprar
MateComB=TotalMateB+inventarioInicialMB
print("El Total de Materiales a comprar de 1er semestre es: ",MateComB)
MateComB1=TotalMateB1+inventarioInicialMB1
print("El Total de Materiales a comprar de 2do semestre es: ",MateComB1)
TotalCompB2016=TotalMateB2016+inventarioInicialMBTotal2016
print("El Total de MaterialesA a Comprar es: ",TotalMateB2016)
#Material B Precio de Compra
PrecioCompB=int(input("Cual sera el precio de compra del 1er semestre del Material B: "))
PrecioCompB1=int(input("Cual sera el precio de compra del 2do semestre del Material B: "))
#Material B Total de Material en $
TotalmaterialMB=MateComB+PrecioCompB
print("El Total de Material B en dinero de 1er semestre es",TotalmaterialMB)
TotalmaterialMB1=MateComB1+PrecioCompB1
print("El Total de Material B en dinero de 2do semestre es",TotalmaterialMB1)
TotalmaterialMB2016=TotalmaterialMB+TotalmaterialMB1
print("El Total de MaterialesB en dinero es",TotalmaterialMB2016)
#Material C
print( " Material C " )
RequeriMaterialesC=SumaTotalC
RequeriMaterialesC1=SumaTotalCC
print("Los Requerimientos de Materiales en el 1er semestre son" ,
RequeriMaterialesC)
print("Los Requerimientos de Materiales en el 2do semestre son" ,
RequeriMaterialesC1)
print("Los Requerimientos totales son" , SumaC)
#Material A Inventario final
inventariofinalMC=int(input("Ingresa la cifra que genero en el inventario final del 1er semestre: "))
print("El inventario final del 1 semestre es",inventariofinalMC)
inventariofinalMC1=int(input("Ingresa la cifra que genero en el inventario final del 2do semestre: "))
print("El inventario final del 2 semestre es",inventariofinalMC1)
inventariofinalMCTotal2016=inventariofinalMC1
print("El inventario final total es",inventariofinalMCTotal2016)
#Material C Total de Materiales
TotalMateC=RequeriMaterialesC+inventariofinalMC
print("El Total de Materiales de 1er semestre es",TotalMateC)
TotalMateC1=RequeriMaterialesC1+inventariofinalMC1
print("El Total de Materiales de 2do semestre es",TotalMateC1)
TotalMateC2016=SumaC+inventariofinalMCTotal2016
print("El Total de Materiales es",TotalMateC2016)
#Material C Inventario Inicial
inventarioInicialMC=int(input("Ingresa la cifra que genero en el inventario inicial del 1er semestre: "))
print("El inventario inicial del 1 semestre es",inventarioInicialMC)
inventarioInicialMC1=int(input("Ingresa la cifra que genero en el inventario inicial del 2do semestre: "))
print("El inventario inicial del 2 semestre es",inventarioInicialMC1)
inventarioInicialMCTotal2016=inventariofinalMC
print("El inventario inicial total es",inventarioInicialMCTotal2016)
#Material C Material a Comprar
MateComC=TotalMateC+inventarioInicialMC
print("El Total de Materiales a comprar de 1er semestre es: ",MateComC)
MateComC1=TotalMateC1+inventarioInicialMC1
print("El Total de Materiales a comprar de 2do semestre es: ",MateComC1)
TotalCompC2016=TotalMateC2016+inventarioInicialMCTotal2016
print("El Total de MaterialesC a Comprar es",TotalMateC2016)
#Material C Precio de Compra
PrecioCompC=float(input("Cual sera el precio de compra del 1er semestre del Material C: "))
PrecioCompC1=float(input("Cual sera el precio de compra del 2do semestre del Material C: "))
#Material C Total de Material en $
TotalmaterialMC=MateComC+PrecioCompC
print("El Total de Material C en dinero de 1er semestre es: ",TotalmaterialMC)
TotalmaterialMC1=MateComC1+PrecioCompC1
print("El Total de Material C en dinero de 2do semestre es: ",TotalmaterialMC1)
TotalmaterialMC2016=TotalmaterialMC+TotalmaterialMC1
print("El Total de Materiales C en dinero es",TotalmaterialMC2016)
#Compras Totales
CompTotales1er= TotalmaterialMA+TotalmaterialMB+TotalmaterialMC
print("Las compras totales del 1er semestre son : ", CompTotales1er)
CompTotales2do= TotalmaterialMA1+TotalmaterialMB1+TotalmaterialMC1
print("Las compras totales del 1er semestre son : ", CompTotales2do)
CompATotales2016=TotalmaterialMA2016+TotalmaterialMB2016+TotalmaterialMC2016
print("Las Compras Totales del 2016 fueron de : " , CompATotales2016)
######6666
#6 Determinacion del saldo de proovedores y flujo de salidas
print("DETERMINACION DEL SALDO DE PROOVEDORES Y FLUJO DE SALIDAS")
SaldoProveedores=int(input( " Cual es el saldo de proveedores del 31-dic-2015? "
))
TotalProveedores2016=SaldoProveedores+CompATotales2016
print( " Sus compras del 2016 fueron de : " , TotalProveedores2016 )
print("********************")
#6.Salidas de efectivo
print(" se pagara el 100% el saldo de proveedores del 2015 : " )
print(SaldoProveedores)
print("se pagara el 50% en las compras del 2016 : ")
pago2016=CompATotales2016*.5
print(pago2016)
TotalSalida2016=SaldoProveedores+pago2016
print(" La salida total de 2016 es: " )
print(TotalSalida2016)
print("********************")
SaldoProveedores2016=TotalProveedores2016-TotalSalida2016
print(" Su saldo de proveedores del 2016 es : ")
print(SaldoProveedores2016)
#7
print("********************************************")
print("PRESUPUESTO MANO DE OBRA")
print("PRODUCTO D Primer Semestre")
horacl=int(input("Dime las horas requeridas por unidades: "))
cl1=(unidadesaproducircl1*horacl)
print("El total de horas requeridas para el Primer Semestre son: ",cl1)
CuotaHoraCL1=int(input("Dime la cuota por hora: "))
importecl1=(cl1*CuotaHoraCL1)
print("El Importe de M.O.D. en el Primer semestre es: ",importecl1)
print("CL Segundo Semestre")
cl2=(unidadesaproducircl2*horacl)
print("El total de Horas requeridas para el Segundo Semestre son: ",cl2)
CuotaHoraCL2=int(input("Dime la cuota por hora: "))
importecl2=(cl2*CuotaHoraCL2)
print("El Importe de M.O.D. en el Segundo semestre es: ",importecl2)
print("PRODUCTO D")
cl3=(unidadesaproducirclTotal2015*horacl)
print("El total de Horas requeridas para el Total son: ",cl3)
CuotaHoraTotal=int(input("Dime la cuota por hora: "))
importeTotal=(cl3*CuotaHoraTotal)
print("El Importe de M.O.D. en TOTAL semestre es: ",importeTotal)
print("CE Primer Semestre")
horace=int(input("Dime las horas requeridas por unidades: "))
ce1=(unidadesaproducirce1*horace)
print("El total de Horas requeridas para el Primer Semestre son: ",ce1)
CuotaHoraCE1=int(input("Dime la cuota por hora: "))
importece1=(ce1*CuotaHoraCE1)
print("El Importe de M.O.D. en el Primer semestre es: ",importece1)
print("CE Segundo Semestre")
ce2=(unidadesaproducirce2*horace)
print("El total de Horas requeridas para el Segundo Semestre son: ",ce2)
CuotaHoraCE2=int(input("Dime la cuota por hora: "))
importece2=(ce2*CuotaHoraCE2)
print("El Importe de M.O.D. en el Segundo semestre es: ",importece2)
print("CE TOTAL")
ce3=(unidadesaproducirceTotal2015*horace)
print("El total de Horas requeridas para el Total son: ",ce3)
CuotaHoraCE1=int(input("Dime la cuota por hora: "))
importeceTotal=(ce3*CuotaHoraCE1)
print("El Importe de M.O.D. en TOTAL semestre es: ",importeceTotal)
print("CR Primer Semestre")
horacr=int(input("Dime las horas requeridas por unidades: "))
cr1=(unidadesaproducircr1*horacr)
print("El total de Horas requeridas para el Primer Semestres son: ",cr1)
CuotaHoraCR1=int(input("Dime la cuota por hora: "))
importecr1=(cr1*CuotaHoraCR1)
print("El Importe de M.O.D. en el primer semestre es: ",importecr1)
print("CR Segundo Semestre")
cr2=(unidadesaproducircr2*horacr)
print("El total de Horas requeridas para el Primer Semestres son: ",cr2)
CuotaHoraCR2=int(input("Dime la cuota por hora: "))
importecr2=(cr2*CuotaHoraCR2)
print("El Importe de M.O.D. en el segundo semestre es: ",importecr2)
print("CALCETINES B TOTAL ")
crTotal=(unidadesaproducircrTotal2015*horacr)
print("El total de Horas requeridas para el Primer Semestres son: ",crTotal)
CuotaHoraTotal=int(input("Dime la cuota por hora: "))
importeCRTotal=(crTotal*CuotaHoraTotal)
print("El Importe de M.O.D. TOTAL es: ",importeCRTotal)
TotalHoras=(cl1+ce1+cr1)
TotalMOD=(importecl1+importece1+importecr1)
print("El total de horas requeridas en el Primer Semestre son: ",TotalHoras)
print("El total de M.O.D. totales en el Primer Semestre son: ", TotalMOD)
TotalHoras2=(cl2+ce2+cr2)
TotalMOD2=(importecl2+importece2+importecr2)
print("El total de horas requeridas en el Segundo Semestre son: ",TotalHoras2)
print("El total de M.O.D. totales en el Segundo Semestre son: ", TotalMOD2)
TotalHorasTotales=(cl3+ce3+crTotal)
TotalMODTotal=(importeTotal+importeceTotal+importeCRTotal)
print("El total de horas requeridas en Total son: ",TotalHorasTotales)
print("El total de M.O.D. totales en Total son: ", TotalMODTotal)
print("*********************************************************")
#8
print("PRESUPUESTO DE GASTOS INDIRECTOS DE FABRICACION")
#PRIMER SEMESTRE
print("1ER SEMESTRE")
Depreciacion1=float(input("Cuanto fue la depreciacion del Primer Semestre?: "))
Seguros1=float(input("Cuanto fue lo del seguro?: "))
Mantenimiento1=float(input("Cuanto fue de mantenimiento?: "))
Energeticos1=float(input("Cuanto fue de energeticos?: "))
Varios1=float(input("Cuanto fue de gastos varios?: "))
Suma=(Depreciacion1 + Seguros1 + Mantenimiento1 + Energeticos1 + Varios1)
print("Este fue el total del GIF el Primer semestre", Suma)
#SEGUNDO SEMESTRE
print("2DO SEMESTRE")
Depreciacion2=float(input("Cuanto fue la depreciacion del Segundo Semestre?: "))
Seguros2=float(input("Cuanto fue lo del seguro?: "))
Mantenimiento2=float(input("Cuanto fue de mantenimiento?: "))
Energeticos2=float(input("Cuanto fue de energeticos?: "))
Varios2=float(input("Cuanto fue de gastos varios?: "))
Suma2=(Depreciacion2+Seguros2+Mantenimiento2+Energeticos2+Varios2)
print("Este fue el total del GIF el Segundo semestre", Suma2)
#TOTAL 2015
print("TOTAL")
Depreciacion3=(Depreciacion1+Depreciacion2)
print("El total de Depreciacion fue de: ", Depreciacion3)
Seguros3=(Seguros1+Seguros2)
print("El total de Seguros fue de: ", Seguros3)
Mantenimiento3=(Mantenimiento1+Mantenimiento2)
print("El total de Mantenimiento fue de: ", Mantenimiento3)
Energeticos3=(Energeticos1+Energeticos2)
print("El total de Energeticos fue de: ", Energeticos3)
Varios3=(Varios1+Varios2)
print("El total de Varios fue de: ", Varios3)
DepreciacionTotal=(Depreciacion3+Seguros3+Mantenimiento3+Energeticos3+Varios3)
print("El total del GIF fue de: ", DepreciacionTotal)
CostoHoraGIF=(DepreciacionTotal-TotalHorasTotales)
print("El costo por Hora de GIF sera de", CostoHoraGIF)
######999
#9 Presupuesto de Gastos de Operaciones
print("PRESUPUESTO DE GASTOS DE OPERACIONES")
#Depreciacion
depreciaciongo1=int(input("Dime la cifra de la depreciacion del 1er semestre: "))
depreciaciongo2=int(input("Dime la cifra de la depreciacion del 2do semestre: "))
depreciaciongototal2015=depreciaciongo1 + depreciaciongo2
print("el total del 2015 de las depreciaciones son ",depreciaciongototal2015)
#SueldosySalarios
sueldosysalariosgo1=int(input("Dime los sueldos y salarios del 1er semestre: "))
sueldosysalariosgo2=int(input("Dime los sueldos y salarios del 2do semestre: "))
sueldosysalariosgototal2015=sueldosysalariosgo1 + sueldosysalariosgo2
print("los sueldos y salarios totales son ",sueldosysalariosgototal2015)
#Comisiones
comisionesgo1=suma*0.1
comisionesgo1=int(input("Dime los sueldos y salarios del 1er semestre: "))
comisionesgo2=suma2*0.1
comisionesgo2=int(input("Dime los sueldos y salarios del 2do semestre: "))
comisionesgototal2015=comisionesgo1 + comisionesgo2
print("los sueldos y salarios totales son ",comisionesgototal2015)
#Varios
variosgo1=int(input("Dime la cifra del 1er semestre: "))
variosgo2=int(input("Dime la cifra del 2do semestre: "))
variosgototal2015=variosgo1 + variosgo2
print("el total del 2015 de las depreciaciones son ",variosgototal2015)
#interesesporpbligaciones
interesesporobligacionesgo1=int(input("Dime la cifra del 1er semestre: "))
interesesporobligacionesgo2=int(input("Dime la cifra del 2do semestre: "))
interesesporobligacionesgototal2015=interesesporobligacionesgo1+interesesporobligacionesgo2
print("el total del 2015 de las depreciaciones son",interesesporobligacionesgototal2015)
#TotalGastosOperacion
totalgastosoperacionesgo1=depreciaciongo1 + sueldosysalariosgo1+comisionesgo1 + variosgo1 + interesesporobligacionesgo1
print("el total de gastos de operacion del 1 semestre son",totalgastosoperacionesgo1)
totalgastosoperacionesgo2=depreciaciongo2 + sueldosysalariosgo2+comisionesgo2 + variosgo2 + interesesporobligacionesgo2
print("el total de gastos de operacion del 2 semestre son",totalgastosoperacionesgo2)
totalgastosoperaciongototal2015=depreciaciongototal2015+sueldosysalariosgototal2015 + comisionesgototal2015 + variosgototal2015 +interesesporobligacionesgototal2015
print("el total de gastos de operacion del 2015 son",totalgastosoperaciongototal2015)
####10
#10 Determinacion del costo unitario de productos terminados
print("DETERMINACION DEL COSTO UNITARIO DE PRODUCTOS TERMINADOS")
#Producto CL
print ( "Producto D" )
print("material A")
print("estas son las unidades de material A: ", materialA)
print("este es el costo de material A: ", PrecioCompA)
CostototalA=PrecioCompA*materialA
print("El costo total de material A es: ", CostototalA)
print("Material B")
print("estas son las unidades de material B: ", materialB)
print("este es el costo de material B: ", PrecioCompB1)
CostototalB=PrecioCompB1*materialB
print("El costo total de material B es: ", CostototalB)
print("Material C")
print("estas son las unidades de material C: ", materialC)
print("este es el costo de material C: ", PrecioCompC1)
CostototalC=PrecioCompC1*materialC
print("El costo total de material C es: ", CostototalC)
print("Mano de obra")
print("Costo de la mano de obra: ", CuotaHoraCL1)
print("Cantidad de horas laboradas: ", horacl)
CostototalHoracl=CuotaHoraCL1*horacl
print("El costo total de la mano de obra es: ", CostototalHoracl)
print("Gastos Indirectos de Fabricacion: ")
print("Costo del GIF es: ", CostoHoraGIF)
print("Cantidad de horas laboradas: ", horacl)
CostototalHoraGIF=CostoHoraGIF*horacl
print("El costo total del GIF es: ", CostototalHoraGIF)
#SUMAS Costos Unitarios
sumacl=(PrecioCompA1+PrecioCompB1+PrecioCompC1+CuotaHoraCL1+CostoHoraGIF)
print("El Costo Unitario de Costo es: ", sumacl)
cantidadcl=(materialA+materialB+materialC+horacl+horacl)
print("El Costo Unitario de Cantidad es: ", cantidadcl)
costounitario=(CostototalA+CostototalB+CostototalC+CostototalHoracl+CostototalHoraGIF)
print("El Total del Costo Unitario es: ", costounitario)
print("****************")
print( "Producto DI" )
print("material A")
print("estas son las unidades de material A: ", materialCE)
print("este es el costo de material A: ", PrecioCompA1)
CostototalA2=PrecioCompA1*materialCE
print("El costo total de material A es: ", CostototalA2)
print("Material B")
print("estas son las unidades de material B: ", materialCEB)
print("este es el costo de material B: ", PrecioCompB1)
CostototalB2=PrecioCompB1*materialCEB
print("El costo total de material B es: ", CostototalB2)
print("Material C")
print("estas son las unidades de material C: ", materialCC)
print("este es el costo de material C: ", PrecioCompC1)
CostototalC2=PrecioCompC1*materialCC
print("El costo total de material C es: ", CostototalC2)
print("Mano de obra")
print("Costo de la mano de obra: ", CuotaHoraCL1)
print("Cantidad de horas laboradas: ", horace)
CostototalHoraCL2=CuotaHoraCL1*horace
print("El costo total de la mano de obra es: ", CostototalHoraCL2)
print("Gastos Indirectos de Fabricacion: ")
print("Costo del GIF es: ", CostoHoraGIF)
CostototalHoraGIF2=CostoHoraGIF*horace
print("El costo total del GIF es: ", CostototalHoraGIF2)
#SUMAS Costos Unitarios
sumacl=(PrecioCompA1+PrecioCompB1+PrecioCompC1+CuotaHoraCL1+CostoHoraGIF)
print("El Costo Unitario de Costo es: ", sumacl)
cantidadce=(materialCE+materialCEB+materialCC+horace+horace)
print("El Costo Unitario de Cantidad es: ", cantidadce)
costounitarioce=(CostototalA2+CostototalB2+CostototalC2+CostototalHoraCL2+CostototalHoraGIF2)
print("El Total del Costo Unitario es: ", costounitarioce)
print("*****************")
print("Producto Z")
print("material A")
print("estas son las unidades de material A: ", materialCR)
print("este es el costo de material A: ", PrecioCompA1)
CostototalA3=PrecioCompA1*materialCR
print("El costo total de material A es: ", CostototalA3)
print("Material B")
print("estas son las unidades de material B: ", materialCRB)
print("este es el costo de material B: ", PrecioCompC1)
CostototalB3=PrecioCompC1*materialCRB
print("El costo total de material B es: ", CostototalB3)
print("Material C")
print("estas son las unidades de material C: ", materialCC3)
print("este es el costo de material C: ", PrecioCompC1)
CostototalC3=PrecioCompC1*materialCC3
print("El costo total de material C es: ", CostototalC3)
print("Mano de obra")
print("Costo de la mano de obra: ", CuotaHoraCL1)
print("Cantidad de horas laboradas: ", horacr)
CostototalHoraCL3=CuotaHoraCL1*horacr
print("El costo total de la mano de obra es: ", CostototalHoraCL3)
print("Gastos Indirectos de Fabricacion")
print("Costo del GIF es: ", CostoHoraGIF)
CostototalHoraGIF3=CostoHoraGIF*horacr
print("El costo total del GIF es: ", CostototalHoraGIF3)
#SUMAS Costos Unitarios
sumacl=(PrecioCompA1+PrecioCompB1+PrecioCompC1+CuotaHoraCL1+CostoHoraGIF)
print("El Costo Unitario de Costo es: ", sumacl)
cantidadcr=(materialCR+materialCRB+materialCC3+horacr+horacr)
print("El Costo Unitario de Cantidad es: ", cantidadcr)
costounitariocr=(CostototalA3+CostototalB3+CostototalC3+CostototalHoraCL3+CostototalHoraGIF3)
print("El Total del Costo Unitario es: ", costounitariocr)
####11
# 11. Valuación de Inventarios Finales
#Inventario Final de Materiales
print("Inventario Final de Materiales")
print("Material A")
print(" Las unidades del material A es : " , inventariofinalMA1)
print(" Su costo unitario es : " , PrecioCompA1)
CostoTotalA11=inventariofinalMA1+PrecioCompA1
print(" Su Costo Total es : " , CostoTotalA11)
print("Material B")
print(" Las unidades del material B es : " , inventariofinalMB1)
print(" Su costo unitario es : " , PrecioCompB1)
CostoTotalB11=inventariofinalMB1+PrecioCompB1
print(" Su Costo Total es : " , CostoTotalB11)
print("Material C")
print(" Las unidades del material C es : " , inventariofinalMC1)
print(" Su costo unitario es : " , PrecioCompC1)
CostoTotalC11=inventariofinalMC1+PrecioCompC1
print(" Su Costo Total es : " , CostoTotalC11)
print("Inventario Final de Materiales")
UnidadesTotal11=inventariofinalMA1+inventariofinalMB1+inventariofinalMC1
print("Sus Unidades Totales son : " , UnidadesTotal11)
CostosUnitaTo11=PrecioCompA1+PrecioCompB1+PrecioCompC1
print("Sus Costos Unitarios Totales son : " , CostosUnitaTo11)
CostoTotal11=CostoTotalA11+CostoTotalB11+CostoTotalC11
print("Sus Costos Totales son : " , CostoTotal11)
#Inventario Final de Producto Terminado
print("Inventario Final de Producto Terminado")
print("Material D")
print(" Las unidades del material A es : " , inventariofinalcl2)
print(" Su costo unitario es : " , costounitario)
CostoTotalA1A1=inventariofinalMA1+PrecioCompA1
print(" Su Costo Total es : " , CostoTotalA1A1)
print("Material Di")
print(" Las unidades del material B es : " , inventariofinalce2)
print(" Su costo unitario es : " , costounitarioce)
CostoTotalBB11=inventariofinalMB1+PrecioCompB1
print(" Su Costo Total es : " , CostoTotalBB11)
print("Material Z")
print(" Las unidades del material C es : " , inventariofinalcr2)
print(" Su costo unitario es : " , costounitariocr)
CostoTotalCC11=inventariofinalMC1+PrecioCompC1
print(" Su Costo Total es : " , CostoTotalCC11)
print("Inventario Final de Producto Terminado")
Unidades1Total11=inventariofinalcl2+inventariofinalce2+inventariofinalcr2
print("Sus Unidades Totales son : " , Unidades1Total11)
Costos1UnitaTo11=costounitario+costounitarioce+costounitariocr
print("Sus Costos Unitarios Totales son : " , Costos1UnitaTo11)
Costo1Total11=CostoTotalA1A1+CostoTotalBB11+CostoTotalCC11
print("Sus Costos Totales son : " , Costo1Total11)
#ll.Presupuesto Financiero Laboratorios REgionales S.A.
# Estado de Costo de Produccion y Ventas
print("Estado de Costo de Produccion y Ventas")
print("Presupuesto del 1 de Enero al 31 de Diciembre del 2016")
SaldoInMA=int(input("Cual es el Saldo Inicial de Materiales: "))
ComprasmaLAB=CompATotales2016
print("Las Compras de Materiales fueron de : ", CompATotales2016)
MaterialDispLAB=SaldoInMA+ComprasmaLAB
print("Su material disponible es de : ", MaterialDispLAB)
print("El inventario final de materiales fue de : ", CostoTotal11)
MaterialUtlLAB=MaterialDispLAB-CostoTotal11
print ("Los Materiales Utilizados fueron de : ", MaterialUtlLAB)
print("La Mano de Obra Directa fue de : ", TotalMODTotal)
print("Los gastos de Fabricacion Indirectos fueron de : ", DepreciacionTotal)
CostoProLAB=MaterialUtlLAB+TotalMODTotal+DepreciacionTotal
print("El Costo de Produccion fue de : ",CostoProLAB)
InvInProLAB=int(input("Ingresa el Inventario Inicial de Productos Terminados: "))
TotalProDisLAB=CostoProLAB+InvInProLAB
print("El Total de Produccion Disponible es de : " ,TotalProDisLAB)
print("El Inventario Final de Productos Terminados fue de : ",Costo1Total11)
CostoVentasLAB=TotalProDisLAB-Costo1Total11
print("Su Costo de Ventas fue de : ", CostoVentasLAB)
####ESTADO DE RESULTADOS
print("**********************")
print("Estado de Resultados")
print("El total de Ventas fue de: ",sumatotal)
print("El costo de ventas fue de: ",CostoVentasLAB)
utilidad_bruta=(sumatotal-CostoVentasLAB)
print("La utilidad bruta es: ",utilidad_bruta)
print("El total de gastos de operacion es: ",totalgastosoperaciongototal2015)
utilidad_operacion=(utilidad_bruta-totalgastosoperaciongototal2015)
print("La utilidad de Operacion es: ",utilidad_operacion)
ISR=float(input("Cuanto fue de ISR: "))
ISR_TOTAL=(utilidad_operacion*ISR)
print("El total de ISR es: ",ISR_TOTAL)
PTU=float(input("Cuanto fue de PTU: "))
PTU_TOTAL=(utilidad_operacion*PTU)
print("El total de PTU es: ",PTU_TOTAL)
utilidad_neta=(utilidad_operacion-ISR_TOTAL-PTU_TOTAL)
print("La utilidad neta fue de: ",utilidad_neta)
#FLUJO DE EFECTIVO
print("******************************")
print("Flujo de Efectivo")
saldo_inicial=float(input("Dime el saldo total de efectivo: "))
print("ENTRADAS")
print("La cobranza del 2015 fue de: ",Cobranza2015)
print("La cobranza del 2016 fue de: ",Cobranza2016)
cobranzatotal=(Cobranza2015+Cobranza2016)
print("El total de entradas es de: ",cobranzatotal)
efectivo_disponible=(saldo_inicial+cobranzatotal)
print("El efectivo disponible es de: ",efectivo_disponible)
print("SALIDAS")
print("Los saldos de proveedores del 2016 fueron de: ",SaldoProveedores)
print("Los saldos de proveedores del 2015 fueron de: ",pago2016)
print("El pago total de Mano De Obra Directa fue de: ",TotalMODTotal)
gastosindirectostotal=(DepreciacionTotal-Depreciacion3)
print("Los gastos indirectos fueron: ",gastosindirectostotal)
gastooperacion=(totalgastosoperaciongototal2015-depreciaciongototal2015)
print("Los gastos de operacion fueron: ",gastooperacion)
maquinaria=float(input("Cual fueron los gastos de maquinaria o de activo fijo?: "))
ISR2014=float(input("Cual fue el ISR del 2015?: "))
ISR2015=float(input("Cual fue el ISR del 2016?: "))
TotalSalidas=(SaldoProveedores+pago2016+TotalMODTotal+gastosindirectostotal
+gastooperacion+maquinaria+ISR2014+ISR2015)
print("El Total de las Salidas fue de: ",TotalSalidas)
FlujoTotal=(efectivo_disponible-TotalSalidas)
print("El Flujo Total es de: ",FlujoTotal)
#BALANCEGENERAL
#Presupuesto31Diciembre2016
print("Maquilados Mexicanos S.A de C.V")
print("Balance General")
print("Activo")
print("Circulante")
efectivomxbg=FlujoTotal
print("El activo del efectivo es: ",efectivomxbg)
clientesmxbg=SaldoClientes2016
print("El activo de los clientes es: ",clientesmxbg)
deudoresmxbg=int(input("Ingresa la cifra de los deudores: "))
print("El activo de los deudores son",deudoresmxbg)
funcionariosyempleadosmxbg=int(input("Ingresa la cifra de los funcionarios y empleados: "))
print("El activo de los funcionarios y empleados es: ",funcionariosyempleadosmxbg)
inventariomaterialesmxbg=CostoTotal11
print("El activo del inventario de materiales es: ",inventariomaterialesmxbg)
inventarioproductoterminadomxbg=Costo1Total11
print("El activo del inventario de producto terminado es: ",inventarioproductoterminadomxbg)
totalactivocirculantemxbg=efectivomxbg + clientesmxbg + deudoresmxbg + inventariomaterialesmxbg + inventarioproductoterminadomxbg
print("El total del activo circulante es",totalactivocirculantemxbg)
print("Activo")
print("No Circulante")
terrenomxbg=int(input("Ingresa la cifra de los terrenos: "))
print("el activo de los terrenos es: ",terrenomxbg)
PlantayEquipoBG=1500000
plantayequipomxbg=maquinaria+PlantayEquipoBG
print("el activo de la planta y equipo es: ",plantayequipomxbg)
DeprAcuBG=650000
depreciacionacumuladamxbg=DeprAcuBG+Depreciacion3+depreciaciongototal2015
print("el activo de la depreciacion acumulada es: ",depreciacionacumuladamxbg)
totalactivonocirculantemxbg=terrenomxbg + plantayequipomxbg + depreciacionacumuladamxbg
print("el total del activo No Circulante es: ",totalactivonocirculantemxbg)
totalactivomxbg= totalactivocirculantemxbg + totalactivonocirculantemxbg
print("el total del activo es: ",totalactivomxbg)
print("Pasivo")
print("Corto Plazo")
proveedoresmxbg=SaldoProveedores2016
print("el pasivo de los proveedores es: ",proveedoresmxbg)
documentosxpagarmxbg=int(input("Ingresa la cifra de los documentos por pagar:"))
print("el activo de los documentos por pagar son",documentosxpagarmxbg)
isrxpagarmxbg=int(input("Ingresa la cifra del isr por pagar: "))
print("el activo del isr por pagar es: ",isrxpagarmxbg)
ptuxpagarmxbg=PTU_TOTAL
print("el pasivo del ptu por pagar es ", ptuxpagarmxbg)
totalpasivocortoplazomxbg=proveedoresmxbg + documentosxpagarmxbg +isrxpagarmxbg + ptuxpagarmxbg
print("el total del pasivo a corto plazo es ",totalpasivocortoplazomxbg)
print("Largo Plazo")
PrestBancariosBG=int(input("Ingresa los Prestamos Bancarios: "))
TotalPLPBG=PrestBancariosBG
print("El Total de Pasivo Largo Plazo es de : ", TotalPLPBG)
PasivoTotalBG=totalpasivocortoplazomxbg+TotalPLPBG
print("Capital Contable")
CapAporBG=int(input("Ingresa el Capital Aportado: "))
CapGanBG=int(input("Ingresa el Capital Ganado: "))
UtiEjerBG=utilidad_neta
print("La utilidad del Ejercicio fue de : " , UtiEjerBG)
TotalCCBG=UtiEjerBG+CapGanBG+CapAporBG
print("El total de Capitable Contable es de : " , TotalCCBG)
SumaPasyCapBG=TotalCCBG+PasivoTotalBG
print("La suma de Pasivo y Capital es de: ", SumaPasyCapBG)
print("GRACIAS!!!!")