// -*-coding:utf-8-*-

function check_and_go()
{
    ip_box = document.getElementById('query_box_ip');
    ip = ip_box.value;

    // 正确性检查
    format_is_ok = false;
    error_message = '';
    if(ip == '') {
        format_is_ok = false;
        error_message = '请输入IP地址后再点击查询按钮';
    } else {
        if(/[0-9]/.test(ip)) {  // 全为数字，合法
            format_is_ok = true;
            error_message = '';
        } else if(/[0-9.]/.test(ip)) { // 点分十进制，解析各段
            ip_array = ip.split(".");
            format_is_ok = (
                (ip_array.length == 4) &&
                    ((ip_array[0].length != 0) && (ip_array[0] >= 0) && (ip_array[0] <= 255)) &&
                    ((ip_array[1].length != 0) && (ip_array[1] >= 0) && (ip_array[1] <= 255)) &&
                    ((ip_array[2].length != 0) && (ip_array[2] >= 0) && (ip_array[2] <= 255)) &&
                    ((ip_array[3].length != 0) && (ip_array[3] >= 0) && (ip_array[3] <= 255))
            );
            error_message = '请输入正确的IP地址';
        } else {
            format_is_ok = false;
            error_message = '请输入正确的IP地址';
        }
    }

    error_msg = document.getElementById('query_box_error_msg');
    if(format_is_ok) {
        error_msg.style.display = 'none';
        error_msg.innerHTML = '';
        document.location='/ip/' + ip;
    } else {
        error_msg.style.display = '';
        error_msg.innerHTML = error_message;
        ip_box.focus();
        ip_box.select();
    }
    return false;
}

// 页面加载后，聚焦到输入框。
ip_box = document.getElementById('query_box_ip').focus();
