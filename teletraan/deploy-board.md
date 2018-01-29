# Views
## webapp/env_views.EnvLandingView
* for these three urls (i.e. they are the same)
  * /env/env_name/
  * /env/env_name/stage_name/
  * /env/env_name/stage_name/deploy/
* templates
  * environs/env_landing.html
    * deploys/deploy_progress.tmpl
      * deploys/deploy_progress_summary.tmpl
      
# logs
* /tmp/deploy_board/
  * access.log

# js
## teletraan-index.js
* deploy-board/deploy_board/static/js/private/teletraan-index.js.
  * Global function calls, that can be called when clicking some buttons, based on ID. This can be use for
* get resources
* creating resources, e.g.
```
$(function () {
        $('#newBuildBtnId').click(function () {
                $('#newBuildModalId').modal();

                $('#createBuildModalBtn').click(function () {
                    var values = $("#values_id").val();
                    var values_array = values.split(",");
                    console.log(value_array);
                        $.ajax({
                                type: "POST",
                                url: "http://xx.xx.xx.xx:8080/v1/builds/create",
                                dataType: 'json',
                                contentType:"application/json;charset=utf-8",
                                data: JSON.stringify({
                                        "name" :$("#name").val(),
                                        "type" :$("#type_id").val(),
                                        "owner" :$("#owner_id").val(),
                                        "values" :values_array,
                                        "description" :$("#description_id").val()
                                }),
                                success: function (data) {
                                    $('#newBuildModalId').modal('toggle');
                         //       window.location = "/xxx/";
                                }
                        });
                });
        });
});
```

