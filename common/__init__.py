import common.input_target as _input
import common.clear_nan as _clearnan
import common.get_forum_name as _get_forum_name
import common.read as _read
import common.out as _out
import common.check as _check
import common.res as _res

input_target = _input.target
get_forum_name = _get_forum_name.get_forum_name

get_data = _read.get_data
get_history = _read.get_history
get_srf = _read.get_srf
get_json = _read.get_json

out_data = _out.out_data
out_history = _out.out_history
out_jindu = _out.out_jindu
out_title = _out.out_title
out_pass = _out.out_pass
write_resault = _out.write_resault

clear_nan = _clearnan.clear_nan

Check = _check.Check
check_forum = _check.check_forum
find_history = _check.find_history
check_repeat = _check.check_repeat
check_black = _check.check_black
check_proce = _check.check_proce
check_in = _check.check_in

Http = _res.Http
