<template>
  <div class="h-screen w-screen max-h-max bg-gray-200 overflow-hidden flex flex-col">
    <Disclaimer class="w-10/12 lg:w-1/2 mt-4 mx-auto"/>
    <ChatWindow class="w-10/12 h-96 flex-grow lg:w-1/2 mt-4 mx-auto rounded-2xl"/>
    <footer class=" bg-purple-300 w-full mx-auto flex h-32 justify-between p-4">
      <input type="text" id="task" placeholder="Type here" class="input input-bordered w-full max-w-xs mx-auto" />
      <input type="file" id="dataset" class="file-input w-full max-w-xs" />
      <button @click="handleQuery" class="btn btn-success">Send</button>
    </footer>
  </div>
</template>

<script setup>
    
async function handleQuery()
{
    const chatWindow = document.getElementById("chat-window");
    const task = document.getElementById("task").value;
    //const dataset = document.getElementById("dataset").value;
    const dataset = "https://firebasestorage.googleapis.com/v0/b/staffier-8863b.appspot.com/o/heart_failure_clinical_records_dataset.csv?alt=media&token=80ba957a-38e8-4c4c-80fa-e6c1324411d9&_gl=1*1ps84zf*_ga*MTI1MDU0NDI5Mi4xNjk5MTMzOTUw*_ga_CW55HF8NVT*MTY5OTEzMzk1MC4xLjEuMTY5OTEzNDAyMS41MS4wLjA."

    // create a new text bubble from the right side
    const uChat = document.createElement("div");
    uChat.classList.add("chat");
    uChat.classList.add("chat-end");
    const uBubble = document.createElement("div");
    uBubble.classList.add("chat-bubble");
    uBubble.innerText = task;
    uChat.appendChild(uBubble);
    chatWindow.appendChild(uChat);

    const sChat = document.createElement("div");
    sChat.classList.add("chat");
    sChat.classList.add("chat-start");
    const sBubble = document.createElement("div");
    sBubble.classList.add("chat-bubble");
    sBubble.innerHTML= "Loading...";
    sChat.appendChild(sBubble);
    chatWindow.appendChild(sChat);

    const res = await fetch(`127.0.0.1:8000/link?task="${task}"&dataset="${dataset}"`);
    console.log(res);

    // using the data, create a new text bubble from the left side
    // data contains "type", "accuracy", "url"
    sBubble.innerHTML = `Model Type: ${res.type}<br>Accuracy: ${res.accuracy}<br>URL: ${res.url}`;
}

</script>