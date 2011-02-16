

function check_and_go(tag)
{
    ip = document.query_box_ip.ip.value;

    if(/[0-9]/.test(ip))
    {
        tag.href="/ip/" + ip + '?f=1';
        return true;
    }
    else
    {
        ip_array = ip.split(".");
        if((ip_array.length == 4) &&
           ((ip_array[0].length != 0) && (ip_array[0] >= 0) && (ip_array[0] <= 255)) &&
           ((ip_array[1].length != 0) && (ip_array[1] >= 0) && (ip_array[1] <= 255)) &&
           ((ip_array[2].length != 0) && (ip_array[2] >= 0) && (ip_array[2] <= 255)) &&
           ((ip_array[3].length != 0) && (ip_array[3] >= 0) && (ip_array[3] <= 255)))
        {
            tag.href="/ip/" + ip + '?f=1';
            return true;
        }
        else
        {
            alert('你输入的IP有误');
            document.query_box_ip.ip.focus();
            return false;
        }
    }
}
