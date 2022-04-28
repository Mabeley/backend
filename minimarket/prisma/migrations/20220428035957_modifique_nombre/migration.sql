/*
  Warnings:

  - You are about to drop the `DetallePedido` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `Pedido` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "DetallePedido" DROP CONSTRAINT "DetallePedido_pedido_id_fkey";

-- DropForeignKey
ALTER TABLE "DetallePedido" DROP CONSTRAINT "DetallePedido_producto_id_fkey";

-- DropForeignKey
ALTER TABLE "Pedido" DROP CONSTRAINT "Pedido_clienteId_fkey";

-- DropTable
DROP TABLE "DetallePedido";

-- DropTable
DROP TABLE "Pedido";

-- CreateTable
CREATE TABLE "pedidos" (
    "id" SERIAL NOT NULL,
    "fecha" DATE NOT NULL,
    "total" DOUBLE PRECISION NOT NULL,
    "estado" "PEDIDO_ESTADO" NOT NULL,
    "process_id" TEXT,
    "clienteId" INTEGER NOT NULL,

    CONSTRAINT "pedidos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "detallePedido" (
    "id" SERIAL NOT NULL,
    "cantidad" DOUBLE PRECISION NOT NULL,
    "sub_total" DOUBLE PRECISION NOT NULL,
    "unidadMedida" "UM_PRODUCTO" NOT NULL,
    "producto_id" INTEGER NOT NULL,
    "pedido_id" INTEGER NOT NULL,

    CONSTRAINT "detallePedido_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "pedidos_id_key" ON "pedidos"("id");

-- CreateIndex
CREATE UNIQUE INDEX "detallePedido_id_key" ON "detallePedido"("id");

-- AddForeignKey
ALTER TABLE "pedidos" ADD CONSTRAINT "pedidos_clienteId_fkey" FOREIGN KEY ("clienteId") REFERENCES "usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "detallePedido" ADD CONSTRAINT "detallePedido_producto_id_fkey" FOREIGN KEY ("producto_id") REFERENCES "productos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "detallePedido" ADD CONSTRAINT "detallePedido_pedido_id_fkey" FOREIGN KEY ("pedido_id") REFERENCES "pedidos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
