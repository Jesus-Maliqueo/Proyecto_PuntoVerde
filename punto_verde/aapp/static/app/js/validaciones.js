const formu = document.getElementById('formu'); //Selecciona formulario por el id
const inputs = document.querySelectorAll('#formu input'); //Selecciona los input de formu (input de html)


const expresiones = {
	usuario: /^[a-zA-Z\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 caracteres.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/, // 7 a 14 numeros.
    rut: /^[0-9]{7,8}[-|‐]{1}[0-9kK]{1}$/, // Validalor estructura rut / 7 a 8 numeros / - exije / un digito mas entre 0y9 o k o K
    direccion: /^.{5,30}$/, // 5 a 30 caracteres.
    tipocont: /^[a-zA-Z]{1}$/,
    peso: /^\d{2,7}$/
    
}


const campos = {
    // Otorga valores falsos a todos los atributos
    rut: false,
    nombre:false,
    direccion :false,
    telefono:false,
    tipocont:false,
    peso:false,
    pass:false,
    email:false,
}


const validarFormu = (e) =>{
    switch (e.target.name){ //Le dice que seleccione el nombre del html input
        case "rut" : //Si en nombre es rut
            validarcampo( expresiones.rut, e.target, 'g_rut' ); //ejecuta funcion Validarcampo solicitando  expresion(restricciones arriba)y cual expresion, envia a quien pertenece (id) y envia grupo (id del div)
            break; //termina el ciclo
        case "primer_nombre" :
            validarcampo(expresiones.nombre, e.target, 'g_pnomb')
            break; 
        case "segundo_nombre" :
            validarcampo(expresiones.nombre, e.target, 'g_snomb')
            break; 
        case "primer_apellido" : 
            validarcampo(expresiones.nombre, e.target, 'g_papell')
            break; 
        case "segundo_apellido" : 
            validarcampo(expresiones.nombre, e.target, 'g_sapell')
            break; 
        case "direccion" : 
            validarcampo(expresiones.direccion, e.target, 'g_dire')
            break; 
        case "telefono" : 
            validarcampo(expresiones.telefono, e.target, 'g_num')
            break; 
        case "tipo_contenedor": 
            validarcampo(expresiones.tipocont, e.target, 'g_tipo')
            break; 
        case "peso" : 
            validarcampo(expresiones.peso, e.target, 'g_peso')
            break; 
        case "contraseña" : 
            validarcampo(expresiones.password, e.target, 'g_contr')
            break; 
        case "email" : 
            validarcampo(expresiones.correo, e.target, 'g_coreo')
            break; 

    }
}






const validarcampo = (expresion, input, campo) => {
    if(expresion.test(input.value)){
        document.getElementById(`${campo}`).classList.remove('form-group-incorrecto'); // elimina nombre de clase
        document.getElementById(`${campo}`).classList.add('form-group-correcto'); // agrega nombre de clase
        campos[campo] = true; // Ootrga valores true a const campos
    } else {
        document.getElementById(`${campo}`).classList.add('form-group-incorrecto');
        document.getElementById(`${campo}`).classList.remove('form-group-correcto');
        campos[campo] = false;
    }
}




inputs.forEach((input)=> {
    input.addEventListener('keyup', validarFormu); //al levantar una tecla hace algo
    input.addEventListener('blur', validarFormu); //al clikear fuera del input hace algo
});

 formu.addEventListener('submit',(e) => { //si todos los campos son verdaderos llenos realiza sumbit
    
     if(campos.rut && campos.nombre && campos.direccion && campos.telefono && campos.tipocont && campos.peso && campos.pass && campos.email ){
        formu.reset();
     }
 })

