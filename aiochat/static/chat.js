try{
    var sock = new WebSocket('ws://' + window.location.host + WS_URL);
}
catch(err){
    var sock = new WebSocket('wss://' + window.location.host + WS_URL);
}

var service_msg = '<div class="service-msg">{text}</div>', msg_template = `
<div class="media-body">
    <div class="media">
        <div class="media-body">
            <em>@{username}</em> <small class="text-muted">| {time}</small>
            <br>{text}
        </div>
    </div>
</div>`, $chatArea = $('.current-chat-area'), $messagesContainer = $('#messages');

function str2color(str){
    var hash = 0;
    for (var i = 0; i < str.length; i++) {
       hash = str.charCodeAt(i) + ((hash << 5) - hash);
    }
    var color = (hash & 0x00FFFFFF).toString(16).toUpperCase();
    return '00000'.substring(0, 6 - color.length) + color;
}

function showMessage(message) {
    /* Append message to chat area */
    console.log(message);
    var data = jQuery.parseJSON(message.data);
    var date = new Date(data.created_at);
    if (data.user) {
        var msg = msg_template
            .replace('{username}', data.user)
            .replace('{text}', data.text)
            .replace('{time}', date);

    } else {
        var msg = service_msg.replace('{text}', data.text);
    }
    $messagesContainer.append('<li class="media">' + msg + '</li>');
    $chatArea.scrollTop($messagesContainer.height());
}

$(document).ready(function(){
    $chatArea.scrollTop($messagesContainer.height());

    $('#send').on('submit', function (event) {
        event.preventDefault();
        var $message = $(event.target).find('input[name="text"]');
        sock.send($message.val());
        $message.val('').focus();
    });

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

    sock.onmessage = showMessage;
});
