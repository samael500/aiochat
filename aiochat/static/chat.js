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

function dateFormat(date) {
    return [date.getFullYear(), date.getMonth() + 1, date.getDate()].join('-') + ' ' +  [date.getHours(), date.getMinutes(), date.getSeconds()].join(':');
}

function showMessage(message) {
    /* Append message to chat area */
    console.log(message);
    var data = jQuery.parseJSON(message.data);
    var date = new Date(data.created_at);
    if (data.cmd) {
        if (data.cmd === 'empty') {
            $messagesContainer.empty();
            return;
        }
    } else if (data.user) {
        var msg = msg_template
            .replace('{username}', data.user)
            .replace('{text}', data.text)
            .replace('{time}', dateFormat(date));

    } else {
        var msg = service_msg.replace('{text}', data.text.split('\n').join('<br />'));
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
        window.location.assign('/');
    };

    sock.onerror = function (error) {
        console.log(error);
    };

    sock.onmessage = showMessage;
});
