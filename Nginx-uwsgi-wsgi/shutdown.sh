for pid in `ps -ef | grep uwsgi | grep -v grep | awk '{print $2}'`
do
    echo killing $pid
    sudo kill -s 9 $pid
done
