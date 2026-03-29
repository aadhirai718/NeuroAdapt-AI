async function send() {
    let res = await fetch("http://127.0.0.1:8000/learn", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            question: document.getElementById("q").value,
            answer: document.getElementById("a").value,
            time_taken: Math.random()*30
        })
    });

    let data = await res.json();
    document.getElementById("out").innerText =
        JSON.stringify(data, null, 2);
}
