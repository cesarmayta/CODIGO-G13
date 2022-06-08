const app = require('./app');

async function main(){
    await app.listen(app.get('port'));
    console.log('servidor en http://localhost:'+ app.get('port'))
}

main();