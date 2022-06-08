const tareaController = {};

const tareaModel = require('../models/tarea.model');

tareaController.getAll = async (req,res)=>{
    const tareas = await tareaModel.find();
    res.json(tareas);
}

tareaController.create = async (req,res)=>{
    const {nombre,estado} = req.body;
    const nuevaTarea = new tareaModel({
        nombre,
        estado
    })
    await nuevaTarea.save();
    res.json(nuevaTarea);
}

module.exports = tareaController;