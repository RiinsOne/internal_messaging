var slugIdNE = parseInt($('#body-id0').val(), 10);

function getjson(json_url) {
    $.ajax({
        url: json_url,
        dataType: 'JSON',
        type: 'GET',

        success: function(data) {
            var verifiedSlug = parseInt(data[0]['slug'], 10);

            for (var i = 0; i <= 9; i++) {

                msgTitle = data[i]['title'];
                msgTitleId = '#title-id' + i;
                $(msgTitleId).html(msgTitle);

                var msgTags = [];
                for (var j = 0; j < data[i].tags.length; j++) {
                    msgTag = data[i].tags[j]['title'];
                    msgTags += '<span>' + msgTag + ' ' + '</span>';
                };

                msgTagsId = '#tags-id' + i;
                $(msgTagsId).html(msgTags);

                msgBody = data[i]['body']
                msgBodyId = '#body-id' + i;
                $(msgBodyId).html(msgBody);
            };

            if (slugIdNE != verifiedSlug) {
                    count(2);
                };

            reWriteSlugIdNE(verifiedSlug);
        }
    });
};
console.log(slugIdNE);

// var json_url = 'http://127.0.0.1:8000/messages-dah/?format=json';

getjson(json_url);

function reWriteSlugIdNE(a) {
    slugIdNE = a;
};

function count(num) {
    divEffect = $(".highlight-effect0").effect("highlight", {color:"#eb6951"}, 3000 );
    setTimeout(function() {
        divEffect;
        if (num > 0) {
            count(num - 1);
        };
    }, 3000);
};

setInterval(getjson, 5000);
