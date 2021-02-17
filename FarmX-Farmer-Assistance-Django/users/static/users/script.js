$('#toggler').click(function () {
    $('#cropdisplay').toggleClass('hide')
});

$('.expandcontent').click(function () {
    let clicks = $(this).data('clicks');

    $(this).parent().children('p').toggleClass('hide');
    if (clicks) {
        $(this).html('&#11167;')
  } else {
        $(this).html('&#11165;')
  }

  $(this).data("clicks", !clicks);
});


// $('div.content-section').children('p.announcement_content')