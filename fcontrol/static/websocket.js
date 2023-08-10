const socket = new WebSocket('ws://127.0.0.1:8000/ws/sensor')
socket.onmessage = receiveMessage
socket.onclose = closeSocket
function closeSocket(event){

}

function receiveMessage(event){
    const data = JSON.parse(event.data)
    console.log('data',data)
    const type = data.type
    console.log('type', type)
    if (type==='sensor_data_handler'){
        sensorDataHandler(data.data)
    }
}
function sensorDataHandler(data){
//    console.log('data',data)
//    const table = document.getElementById('SensorDataTable')
//    console.log('table',table)
//    const tr_1 = document.createElement('tr')
//    table.appendChild(tr_1)
    const temp = document.getElementById('temp')
    const hum = document.getElementById('hum')
    temp.innerText = `Температура: ${data.temperature} °C`
    hum.innerText = `Влажность: ${data.humidity} %`

}
