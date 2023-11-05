<template>
  <div class="h-screen w-screen max-h-max bg-gray-200 overflow-hidden flex flex-col">
    <Disclaimer class="w-10/12 lg:w-1/2 mt-4 mx-auto"/>
    <ChatWindow class="w-10/12 h-96 flex-grow lg:w-1/2 mt-4 mx-auto rounded-2xl"/>
    <footer class="sticky bottom-0 bg-purple-300 w-full mx-auto flex h-32 justify-between p-4">
      <div class="flex flex-row justify-center w-full md:w-1/2 mx-auto">
        <div class="tooltip" data-tip="Type a natural language query">
          <input type="text" id="task" placeholder="Type your query here" class="input input-bordered w-full max-w-xs mx-auto" />
        </div>

        <div class="tooltip" data-tip="Upload your csv dataset">
          <input type="file" id="dataset" class="file-input w-full max-w-xs" />
        </div>
        <button @click="handleQuery" class="btn btn-success">Send</button>
      </div>
    </footer>
  </div>
</template>

<script setup>
    
async function handleQuery()
{
    const chatWindow = document.getElementById("chat-window");
    const task = document.getElementById("task").value;
    //const dataset = document.getElementById("dataset").value;
    let dataset = await fileToDataUrl(document.getElementById("dataset").files[0]);
    // strip the data:text/csv;base64, from the beginning of the dataurl
    dataset = dataset.substring(dataset.indexOf(",") + 1);

    // pad out the dataset dataurl to be a multiple of 4
    dataset = dataset.padEnd(dataset.length + (4 - dataset.length % 4) % 4, "=");


    // create a new text bubble from the right side
    const uChat = document.createElement("div");
    uChat.classList.add("chat");
    uChat.classList.add("chat-end");
    const uBubble = document.createElement("div");
    uBubble.classList.add("chat-bubble");
    uBubble.innerHTML = `${task}<br>Dataset: ${document.getElementById("dataset").files[0].name}`;
    uChat.appendChild(uBubble);
    chatWindow.appendChild(uChat);

    const sChat = document.createElement("div");
    sChat.classList.add("chat");
    sChat.classList.add("chat-start");
    const sBubble = document.createElement("div");
    sBubble.classList.add("chat-bubble");
    sBubble.innerHTML= "<span class='loading loading-dots loading-lg'></span>";
    sChat.appendChild(sBubble);
    chatWindow.appendChild(sChat);

    try
    {
      const body = {task: task, dataset_file: dataset};
      const options =
      {
        "method": "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: body
      }

      const res = await $fetch(`https://python-nlai-service.onrender.com/file`, options);
      // link?task="${task}"&dataset="${dataset}"
      // using the data, create a new text bubble from the left side
      // data contains "type", "accuracy", "url"
      if(res.type !== undefined)
      {
        sBubble.innerHTML = `Model Type: ${res.type}<br>Accuracy: ${(100 * res.accuracy)}%<br><button onclick="window.open('${res.url}', '_blank')" class="btn btn-wide mt-2">Download your tuned model</button>`;
      }
      else
      {
        sBubble.innerHTML = `I'm sorry, I didn't understand that. Could you please rephrase?`;
      }
    }
    catch(err)
    {
      sBubble.innerHTML = `I'm sorry, I didn't understand that. Could you please rephrase?`;
      console.log(err);
    }
    
    
}

async function fileToDataUrl(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader()
    reader.onload = event => resolve(event.target.result)
    reader.onerror = error => reject(error)
    reader.readAsDataURL(file)
  })
}

</script>