var cd_editor_window;

$(document).ready(() => {
    $('#centre-view-button').on('click', () => {
        cd_editor_window.ui.centre_view_action();
    });    
    $('#save-button').on('click', () => {
        cd_editor_window.ui.save_diagram_action();
    });
});
    