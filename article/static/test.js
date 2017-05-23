/**
 * Created by glavie on 03.03.17.
 */

$( document ).ready(
    function() {
        $('#login_form').on('submit', '#login_form', function (e) {
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url:"/auth/login/",
                data: $('#login_form').serializeArray(),
                dataType: 'json',
                success: function () {
                    alert('1');
                    $('.logout_btn').html('Выйти(' + $('#username').val() + ')');
                    $('#logout').removeAttr('hidden');
                    $('#login_form').attr('hidden', 'true');
                },
                error: function () {
                    alert('2');
                    window.location.replace('/auth/login/')
                }
            });
        })
    }
);
<div id="logout" {% if not username %} hidden {% endif %}>
                            <a href="/auth/logout/" class="btn logout_btn">Выйти({{ username }})</a>
                        </div>