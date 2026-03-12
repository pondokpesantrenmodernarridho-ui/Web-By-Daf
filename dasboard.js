async function checkStock(){

let symbol = document.getElementById("stock").value

let res = await fetch(`http://127.0.0.1:8000/analysis/${symbol}`)
let data = await res.json()

document.getElementById("result").innerHTML = `
<h3>${data.symbol}</h3>
<p>Price: ${data.price}</p>
<p>Trend: ${data.trend}</p>
<p>MA20: ${data.MA20}</p>
<p>MA50: ${data.MA50}</p>
`
}
