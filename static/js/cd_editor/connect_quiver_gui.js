var cd_editor_window;

$(document).ready(() => {
    $('#centre-view-button').on('click', () => {
        cd_editor_window.ui.centre_view_action();
    });    
    $('#save-button').on('click', () => {
        cd_editor_window.ui.save_diagram_action();
    });
    $('#select-all-button').on('click', () => {
        cd_editor_window.ui.select_all_action();
    });
    $('#deselect-all-button').on('click', () => {
        cd_editor_window.ui.deselect_all_action();
    });
});
    