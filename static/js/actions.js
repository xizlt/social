$(document).ready(function () {
    "use strict";
    $('a.btn-style').click(function (e) {
        e.preventDefault();
        var itm = $(this)
        var post = itm.data('post')
        var text = $('#text-' + post).val()

        $.post(itm.data('action'),
            {
                post: post,
                text: text
            },
            function (data) {
                $(data).prependTo("#comment-post-id-" + post)
                $('#text-' + post).val("")
            });
    });

    $('a.like').click(function (e) {
        e.preventDefault();
        var like = $(this);
        var id = like.data('id');
        var action = like.data('action');
        var url = like.data('url');
        $.post(url,
            {
                id: id,
                action: action
            },
            function (data) {
                if (data['status'] === 'ok') {
                    var previous_action = like.data('action');
                    var previous_likes = parseInt(like.find('span.count').text());
                    like.data('action', previous_action === 'like' ? 'unlike' : 'like');

                    if (action === 'like') {
                        like.find('i.fa-thumbs-o-up').replaceWith('<i class="fa fa-thumbs-up icon"></i>');
                        like.find('span.count').text(previous_likes + 1);
                    } else {
                        like.find('i.fa-thumbs-up').replaceWith('<i class="fa fa-thumbs-o-up icon"></i>');
                        like.find('span.count').text(previous_likes - 1);
                    }
                }
            }
        );
    });

    $('a.show-messages').click(function (e) {
        e.preventDefault();
        var itm = $(this).data('id')
        $('#comment-post-id-' + itm).toggle();
    });


    $('a.follow-button').click(function (e) {
        e.preventDefault();
        var o = $(this)
        var u = o.data('id')
        var a = o.data('action')
        var url = o.data('url')
        $.post(url,
            {
                id: u,
                action: a
            },
            function (data) {
                if (data['status'] === 'ok') {
                    var previous_action = o.data('action');

                    o.data('action',
                        previous_action === 'follow' ? 'unfollow' : 'follow');
                    o.text(
                        previous_action === 'follow' ? 'Unfollow' : 'Follow');

                }
            }
        );
    });


});

