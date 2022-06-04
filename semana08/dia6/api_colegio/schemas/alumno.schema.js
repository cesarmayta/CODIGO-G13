const Joi = require('joi');

const nombre = Joi.string().min(3).max(100);
const email = Joi.string().email();
const celular = Joi.string().min(8);
const github = Joi.string().uri();

const createAlumnoSchema = Joi.object({
    nombre : nombre.required(),
    email: email.required(),
    celular: celular.optional(),
    github: github.optional()
});

module.exports = {createAlumnoSchema}