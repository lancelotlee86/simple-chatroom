
// $.getJSON(url, data, func)
// 发送一个 GET 请求给 url ，其中 data 对象的内容将以查询参数的形式发送。
// 一旦数据抵达，它将以返回值作为参数执行给定的函数。

// 点击提交用户名按钮
$(document).ready(function() {
  $('input[name=enterChatroom]').bind('click', function() {
    $('#outputDiv').text(' Hello  ' + $('#nameBox').val() + '，欢迎进入聊天室！');
    $('#login').hide();
    $('#chatArea').show();
  });
});

// 提交词条数据
$(document).ready(function() {
  $('input#send').bind('click', function() {
    // 绑定id为send的button。点击后，发送表单数据，并取得json结果，然后操作dom
    var nickname = $('input[id="nameBox"]').val();
    var content = $('input[id="chatroomBox"]').val();
    $.getJSON( $SCRIPT_ROOT +'/ajax/post_chat_info', {
      'nickname': nickname,
      'content': content
      }, function(data) {
    });
    $('#chatroomBox').val('');
  });
});

// 请求聊天内容，并且每2秒刷新一次 chatInfo 框
$(document).ready(function() {
  function refreshChatInfo(){
    console.log('a');
    $.getJSON( $SCRIPT_ROOT + '/ajax/get_chat_history', function(data) {
      $chatInfo = '';
      for( var i = 0; i < data.result.length; i++) {
          $oneChatInfo = data.result[i].nickname + '   ' + data.result[i].timestamp.substring(11,19) + '\n' + data.result[i].content + '\n\n';
          $chatInfo += $oneChatInfo;
      }
      $('#chatInfo').text($chatInfo);
    });
  }
  setInterval(refreshChatInfo, 1000);
});
