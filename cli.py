import datetime
print(Fore.RED,"""                       .
     /        ,,,....           .       //       .                                 //      ***,,. %%.............%(    .        /                                         **,,.%..........@,@..........%                                                **,,.%..............@..............%                                            *,, %   ..  .   .,. .   . ,..   .  ,. %                                        ,,,.%    @/#         #@@@@                #                                      ,..%    . @    #@@@@@ .@@ @@@@@@     @ @   %                                    ...,.  &  (    @@@@@@@  @. @@@@&@@     @.@
  ..%   ,@@,.   @@@@@@@@ @@@@@@@@@@,  ,       %.                                 ,   %   .@     @@@@@@@@@@@@@@@@@@@@@     @ @  %  .                                   %  @. @    @@@@@@@@@@@@@@@@@@@@@     @ @% %...                                   .  &  .@   @@@@@@@@@@@@@@@&@@@@@   (@      .,,                                    %  *@@& @  @@@@@@@@@@@@@@@@@@@   @@ @@  (,,*                                  ,   *   @* @ @% @@@@@@@@@@@@@@@  @@@ *@&   ,,*                                         %        @@@@@@@@@@@@@@@&@(       %.,**  ,                                 ,/ (    %..   @@@@&@@@@@@@@&@@@@@   . %.,,*,*/
             %     @@@@@@@@@@@@@@    %..,,*                                                (       %%@@@@@@@@@@@%%   ...,,                                            /        //       .        .  ..   /*       .                                """)                                                                             print (Fore.GREEN," BY TRHACKNON ")                                              print (Fore.YELLOW,"https://github.com/trhacknon")                               print (Fore.RED,"we are one")
print (Fore.BLUE,"")                                                                                                                                                                                                                                                                                                                #debut                                                                                                                                                            num = input("Entrer le numero avec le code du pays : ")                          msg = input(" Entrez votre message : ")

#envoi du message                                                                                                                                                 resp = requests.post('https://textbelt.com/text',{                                     'phone' : num ,
      'message' : msg ,                                                                'key' : 'textbelt'
})

print(resp.json())

print ("heure d'envoi : ", datetime.datetime.now())

print (Fore.RED,"thanks for using | by trhacknon ")