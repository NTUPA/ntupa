function initEquipmentSelect(id, ct_list, eq_list, eq_selected) {
    for(var i = 0; i < eq_selected.length; ++i) eq_selected[i] = parseInt(eq_selected[i]);

    var selected = [];
    var selectedText = [];
    var elOrigSelect = $('#' + id);
    var elContainer = $('<div id="' + id + '_container"></div>').insertAfter(elOrigSelect);

    var updateSelected = function() {
        selected = [];
        selectedText = [];
        $('.ui-selected').each(function() {
            var id = $(this).data('id');
            selected.push(parseInt(id));
            selectedText.push($(this).html());
        });
        var selectHtml = '';
        for(var i = 0; i < selected.length; ++i) {
            selectHtml += '<option value="' + selected[i] + '">' + selectedText[i] + '</option>';
        }
        elOrigSelect.html(selectHtml);
    };

    var containerHtml = '<div id="' + id + '_tabs"><ul>';
    for(var i = 0; i < ct_list.length; ++i) {
        containerHtml += '<li><a href="#' + id + '_tabs_' + i + '">' + ct_list[i] + '</a></li>';
    }
    containerHtml += '</ul>';
    for(var i = 0; i < ct_list.length; ++i) {
        containerHtml += '<div id="' + id + '_tabs_' + i + '"><ol id="' + id + '_selectable_' + i + '">';
        for(var j = 0; j < eq_list.length; ++j) {
            if(eq_list[j].category != ct_list[i]) continue;
            if(eq_selected.indexOf(eq_list[j].id) >= 0) containerHtml += '<li class="ui-widget-content ui-selected" data-id="' + eq_list[j].id + '">' + eq_list[j].belongs_to + '｜' + eq_list[j].name + '</li>';
            else containerHtml += '<li class="ui-widget-content" data-id="' + eq_list[j].id + '">' + eq_list[j].belongs_to + '｜' + eq_list[j].name + '</li>';
        }
        containerHtml += '</ol></div>';
    }
    elContainer.html(containerHtml);

    $('#' + id + '_tabs').tabs();
    for(var i = 0; i < ct_list.length; ++i) {
        $('#' + id + '_selectable_' + i).selectable({
            stop: function() {
                updateSelected();
            }
        }).on('selectablestart', function(event, ui) {
            event.originalEvent.ctrlKey = true;
        });
    }

    $('form').submit(function() {
        $('option', elOrigSelect).attr('selected', 'selected');
        return true;
    });

    updateSelected();
}