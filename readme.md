task job django
1. header nav and footer broken on search
2. give all users the ability to reset their password
3. homepage - standardize image height
4. lock menu to top of page

kirim ke swdev.bali@gmail.com

1. using django template
if you do not want to include navbar and footer headers in the search template, then separated in the base.html template with the navbar header template and footer. so in the search template simply use {% extends 'base.html'%} without the navbar header template and footer included.

2. reset django password, has default library and easy in its application. can override using password_reset on django.contrib.auth. 
then, will reset with password_reset_done then get token for password_reset_confirm, then password_reset_complete for finished it.

3. standardize image height on homapage can using tag height="200px" on img tag

4. menu navbar have lock with css static template override css style="position:fixed; right:0; left:0; z-index:1030;" on navbar tag