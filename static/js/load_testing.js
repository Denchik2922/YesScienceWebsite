let balls = 0
        let all_balls = 0
        let count_test = document.getElementById('count_test').innerText

        function check(num) {
            $(".btn_next").css('display','inline-flex')
            balls = num
        }

        $('#start_test').click(function () {
            $('#start_test_menu').css('display', 'none')
            $('#test_page').css('display', 'block')
        })

        function ajaxRequest(page_url) {
            $.ajax({
                url: page_url,
                type: 'GET',
                success: (data) => {
                    $('.testing_content').empty()
                    $('.testing_content').append($(data).filter('.testing_content').html())
                }
            })
        }

        function update_status() {
            all_balls += balls;
            console.log(all_balls);
            if (count_test == all_balls) {
                status = 'Специалист'
            }
            else if (Math.round(count_test / 2) <= all_balls) {
                status = 'Знаток'
            }
            else if (Math.round(count_test / 4) <= all_balls || all_balls == 0 ) {
                status = 'Новичек'
            }
            document.getElementById("status").value = status


        }


        function Test() {
            $('.page_obj').each((index, el) => {
                $(el).click((e) => {
                    e.preventDefault()
                    let page_url = $(el).attr('href')
                    page_url = 'http://127.0.0.1:8000/testing/' + page_url

                    $("input[name='test']").each(function () {
                        if ($(this).prop('checked')) {

                            ajaxRequest(page_url)
                        }

                    })

                })
            })
        }

        $(document).ready(function () {

            update_status()
            Test()
        })

        $(document).ajaxStop(function () {

            update_status()
            Test()
        })