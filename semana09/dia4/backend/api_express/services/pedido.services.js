const MysqlLib = require('../lib/mysql.lib');

class PedidoService{

    constructor(){
        this.sql = new MysqlLib();
    }

    async create({pedido}){
        const sqlCreatePedido = `
        insert into tienda_pedido(fecha,nro,estado,cliente_id)
        values ('${pedido.fecha}','${pedido.nro}','solicitado','${pedido.cliente_id}')
        `

        await this.sql.querySql(sqlCreatePedido);
        const sqlPedidoId = 'select id from tienda_pedido order by id desc limit 1';
        const resultPedidoId = await this.sql.querySql(sqlPedidoId);
        //obtenemos el id del pedido
        const pedidoId = resultPedidoId[0].id;

        //registramos los detalles del pedido
        pedido.productos.map(async (prod)=>{
            const sqlcreatePedidoDetalle = `
            insert into tienda_pedidodetalle(pedido_id,producto_id,precio,cantidad)
            values ('${pedidoId}','${prod.producto_id}','${prod.precio}','${prod.cantidad}')
            `;
            console.log(sqlcreatePedidoDetalle);
            await this.sql.querySql(sqlcreatePedidoDetalle);
        })

        const nuevoPedido = {
            id:pedidoId
        }
        return nuevoPedido;
    }

}

module.exports = PedidoService;