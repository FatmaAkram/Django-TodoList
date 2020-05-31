function toggleMark(obj,id){
    clickedTask = $(obj).parents('label');
    textDecoration = clickedTask.css('text-decoration-line');
    reqType = (textDecoration === 'line-through') ?  'uncomplete' : 'complete'
    $.ajax({
        type: 'POST',
        url: `/todos/${reqType}`,
        data: {
            id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            clickedTask.toggleClass('completed');
        },
        error: function (error) {
            throw new Error(`Error!: ${error['statusText']}`);
        }
    })
}
