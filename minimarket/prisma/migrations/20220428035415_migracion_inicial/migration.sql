-- CreateEnum
CREATE TYPE "USUARIO_ROL" AS ENUM ('ADMINISTRADOR', 'CLIENTE');

-- CreateEnum
CREATE TYPE "UM_PRODUCTO" AS ENUM ('KG', 'UNIDAD');

-- CreateEnum
CREATE TYPE "CATEGORIA_PRODUCTO" AS ENUM ('VERDURAS', 'FRUTA', 'ELECTRODOMESTICO', 'LIMPIEZA', 'OTROS');

-- CreateEnum
CREATE TYPE "PEDIDO_ESTADO" AS ENUM ('CREADO', 'ACEPTADO', 'PAGADO', 'ERROR');

-- CreateTable
CREATE TABLE "usuarios" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "rol" "USUARIO_ROL" NOT NULL DEFAULT E'CLIENTE',
    "validado" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "productos" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "precio" DOUBLE PRECISION NOT NULL,
    "unidad_medida" "UM_PRODUCTO" NOT NULL,
    "categoria" "CATEGORIA_PRODUCTO" NOT NULL,

    CONSTRAINT "productos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Pedido" (
    "id" SERIAL NOT NULL,
    "fecha" DATE NOT NULL,
    "total" DOUBLE PRECISION NOT NULL,
    "estado" "PEDIDO_ESTADO" NOT NULL,
    "process_id" TEXT,
    "clienteId" INTEGER NOT NULL,

    CONSTRAINT "Pedido_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "DetallePedido" (
    "id" SERIAL NOT NULL,
    "cantidad" DOUBLE PRECISION NOT NULL,
    "sub_total" DOUBLE PRECISION NOT NULL,
    "unidadMedida" "UM_PRODUCTO" NOT NULL,
    "producto_id" INTEGER NOT NULL,
    "pedido_id" INTEGER NOT NULL,

    CONSTRAINT "DetallePedido_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_id_key" ON "usuarios"("id");

-- CreateIndex
CREATE UNIQUE INDEX "usuarios_email_key" ON "usuarios"("email");

-- CreateIndex
CREATE UNIQUE INDEX "productos_id_key" ON "productos"("id");

-- CreateIndex
CREATE UNIQUE INDEX "Pedido_id_key" ON "Pedido"("id");

-- CreateIndex
CREATE UNIQUE INDEX "DetallePedido_id_key" ON "DetallePedido"("id");

-- AddForeignKey
ALTER TABLE "Pedido" ADD CONSTRAINT "Pedido_clienteId_fkey" FOREIGN KEY ("clienteId") REFERENCES "usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "DetallePedido" ADD CONSTRAINT "DetallePedido_producto_id_fkey" FOREIGN KEY ("producto_id") REFERENCES "productos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "DetallePedido" ADD CONSTRAINT "DetallePedido_pedido_id_fkey" FOREIGN KEY ("pedido_id") REFERENCES "Pedido"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
