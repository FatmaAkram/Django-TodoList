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
function deleteTask(obj,id){
    clickedTask = $(obj).parents('li');
    $.ajax({
        type: 'POST',
        url: '/todos/delete',
        data: {
            id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (response) {
            clickedTask.remove();
           $('li').length === 0 ? $('.no-tasks').show():'';
        },
        error: function (error) {
            throw new Error(`Error!: ${error['statusText']}`);
        }
    })
}
