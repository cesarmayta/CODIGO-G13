const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const TareaSchema = new Schema({
    nombre:String,
    estado:String
})

module.exports = mongoose.model('tareas',TareaSchema);