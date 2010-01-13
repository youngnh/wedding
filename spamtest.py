import spam
import unittest

class ActualSpamTest(unittest.TestCase):

    spamList = ( 'zCmEsk <a href="http://zohyjsjaxzxl.com/">zohyjsjaxzxl</a>, [url=http://ecugkdlleqsx.com/]ecugkdlleqsx[/url], [link=http://wnugzxkroswn.com/]wnugzxkroswn[/link], http://aqunqenxgyee.com/',
                 'NON sentito parlare di tale http://lacasadicavour.com/kamagra/ - compra cialis generico Si sono errati. Sono in grado di provarlo. Scrivere a me in PM, parlare. http://lacasadicavour.com/cialis/ acquisto cialis online In nessun caso',
                 '<a href=http://notcfootball.org/members/gambling-blackjack-slots-casino-41/default.aspx>gambling blackjack slots casino</a> <a href=http://cpjax.com/dev/Web/members/ultram-order-51/default.aspx>ultram order</a>   <a href="http://community.cmefcu....'
                 'Perdonen, es limpiado http://csalamanca.com/tag/sin-receta/ - viagra generico sildenafil Incomparable topic, me es interesante)))) http://csalamanca.com/ comprar viagra en andorra',
                 "Es conforme, la informacion admirable http://nuevascarreras.com/tag/comprar-cialis/ cialis 20 mg 8 comprimidos Bravo, un'idea brillante e in maniera tempestiva http://nuevascarreras.com/category/cialis-generico/ - cialis 20 mg. </a> gpalmheez...",
                 'Que palabras... La frase fenomenal, admirable http://nuevascarreras.com/comprar-cialis-es/ comprar cialis E il risultato? http://nuevascarreras.com/tag/cialis/ - cialis generico',
                 'And cell-phone wallpapers, too. <a href=" http://members.lycos.co.uk/iseckvn/index.html ">theme free ringtones for lg vx6000 enough</a>   The album artwork is significant as well. <a href=" http://members.lycos.co.uk/teatsvo/index.html ">anything ... ' )

    def testSpamFromSiteIsSpam(self):
        for msg in self.spamList:
            self.assertTrue(spam.isSpam(msg))

class MessageTest(unittest.TestCase):

    msgList = ( "Hurry up and get some info on here!! haha Congrats...can't wait to start planning with you!",
                "YAY!! Finally some good info! Looks great guys...Can't wait!!!",
                "I love you Paige and I can't wait to see you and Nate happily married.",
                "Nate! Did you actually get this WHOLE thing working in a weekend? I am so impressed and reminded why I love you!",
                "Wow - impressive - can't wait for your special day. I agree with paige, I never thought we would see this site so quickly. Great job!!!",
                "...waiting patiently for the new layout!! Can't wait to see how great it looks :)",
                "LOVE the website!!!!! Congrats again love birds. Can't wait to see you both soon!",
                "GREAT WEBSITE! YAY NATE AND PAIGE!",
                "Nate and Paige -    First - CONGRATS!! THIS IS SO STINKING EXCITING!    Now to the serious stuff-    Congratulations to both of you. Paige, you are all grown up (always about 10,000 steps ahead of me) Nate, you are one lucky man to have her (you ...",
                "Nate and Paige,  If Paige is impressed, I am overwheimed (that means overpowered with superior forces)as of Random House Dictionary. May your lives be as well put together as this Web site for many years to come. I love you both, May Gods blessin...",
                "Dear Paige & Nate,  We just got to view your web site; It's great! Loved all the info & the photos. You truly are a wonderful young couple.  Unfortunately, we had booked a Bermuda cruise the week of your wedding Of course it was booked before yo...",
                "I love you both!!!",
                "I'm Thankful for both of you!!!",
                "Congratulations Nate & Paige. Going from vague childhood memories of you when our families did manage to get together to a Save the Date was a nice suprise; its always good to hear that we've pulled another one to the Young side. I wish you and y... "
)

    def testMessagesNotMarkedAsSpam(self):
        for msg in self.msgList:
            self.assertFalse(spam.isSpam(msg))

if __name__ == "__main__":
    unittest.main()

