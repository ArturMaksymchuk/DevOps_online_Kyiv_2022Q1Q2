#!/bin/bash

#-------------3---------
function  list_ip(){
echo "Count requests were there from each ip"
cat $1 | awk '{print$1}'|sort -n|uniq -c|sort -n -r
}
#-------------1---------
function most_ip(){
max=$(list_ip $1 |awk 'NR==2{print$1}')
maxip=$(list_ip $1 |awk 'NR==2{print$2}')

echo " The most requested IP: $maxip with $max requests "
}
#--------2---------
function count_pages(){
awk '{print$7}' $1 |sort -n |uniq -c |sort -n -r
}
function most_page(){
max=$(count_pages $1 |awk 'NR==1{print$1}')
maxp=$(count_pages $1 |awk 'NR==1{print$2}')
echo " The most requested page with $max requests is "
echo $maxp
}
#----------4----------
function nonpages(){
echo  "There are non-existent pages were clients referred to:"
echo " "
awk '($9=="404" ) {print$7}' $1 |sort -n |uniq |sort -n -r
}
#---------5---------
function timelist(){
cat $1 | awk '{print$4}'|awk -F: '{print$2}' |sort -n| uniq -c|sort -n -r
}
function mtime(){
max=$(timelist $1 |awk 'NR==1{print$1}')
maxtime=$(timelist $1 |awk 'NR==1{print$2}')
echo " The most requested time: $maxtime hour with $max requests "
}

#-----------6-----------
function acc_site(){
echo  "There are UA what have accessed the site:"
awk ' {print$12}' $1 |sort -n |uniq| sed  's/"//g'
}

#------------------------------------------------------
most_ip $1
most_page $1
list_ip $1
nonpages $1
mtime $1
acc_site $1



