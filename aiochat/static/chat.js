var msg_template = `
<li class="media">
    <div class="media-body">
        <div class="media">
            <div class="media-body">
                <em>@adsfadsf</em> <small class="text-muted">| 23rd June at 5:00pm</small>
                <br>
                Donec sit amet ligula enim. Duis vel condimentum massa.
                Donec sit amet ligula enim. Duis vel condimentum massa.Donec sit amet ligula enim. 
                Duis vel condimentum massa.
                Donec sit amet ligula enim. Duis vel condimentum massa.
            </div>
        </div>
    </div>
</li>
`, $chatArea = $('.current-chat-area'), $messagesContainer = $('#messages');


function showMessage(message) {
    /* Append message to chat area */
    $messagesContainer.append(msg_template);
    $chatArea.scrollTop($messagesContainer.height());
}

function sendMessage(){
    /* Send message to server */
    var msg = $('#message');
    sock.send(msg.val());
    msg.val('').focus();
}

$(document).ready(function(){

    try{
        var sock = new WebSocket('ws://' + window.location.host + WS_URL);
    }
    catch(err){
        var sock = new WebSocket('wss://' + window.location.host + WS_URL);
    }

    // $('#send').on('submit', function (event) {
    //     event.preventDefault();
    //     showMessage('xxx');
    // });
    $chatArea.scrollTop($messagesContainer.height());

    sock.onopen = function (event) {
        console.log(event);
        console.log('Connection to server started');
    };

    sock.onclose = function (event) {
        console.log(event);
        if(event.wasClean){
            console.log('Clean connection end');
        } else {
            console.log('Connection broken');
        }
    };

    sock.onerror = function (error) {
        console.log(error);
    };

    sock.onmessage = function (data) {
        alert(data.data);
    };
});
