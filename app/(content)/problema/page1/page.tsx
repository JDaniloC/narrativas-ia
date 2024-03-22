import React from 'react';
import { Open_Sans } from 'next/font/google';

import Image from 'next/image';
import { blockMoldure1Img } from '../problema-images';

const openSans = Open_Sans({
  subsets: ['latin'],
  variable: '--open-sans',
})

export default function ProblemaKnownPage() {
  return (
    <div className={`${openSans.className} flex w-auto h-auto`}>
        <div className="text-white text-xl gap-10 max-w-[700px] p-4 flex flex-col mt-20">
            <p>
                Apesar de o termo ter ganhado popularidade com chatbots, como o ChatGPT que você já deve conhecer, essa tecnologia está presente há mais tempo. Na década de 90, programas de xadrez computacional, como o Deep Thought, começaram a desafiar os campeões mundiais.
            </p>
            <p className="text-xl text-right">
                O processo envolve o desenvolvimento de algoritmos e modelos que capacitam os computadores a tomar decisões estratégicas durante uma partida de xadrez.
                <br />
                <br />
                Essa tecnologia também está presente em sistemas de recomendação, como os da Amazon, que utilizam algoritmos de IA para analisar o histórico de compras e comportamento do usuário, oferecendo recomendações personalizadas.
            </p>
            <p>
                A Inteligência Artificial é como ensinamos computadores a pensar e aprender como seres humanos. É uma tecnologia que ajuda as máquinas a entenderem coisas. Mas, assim como tem pontos positivos, também pode ter desafios, como quando queremos manter nossas informações privadas, evitar decisões injustas ou entender como os computadores tomam decisões.
            </p>
        </div>
        <div className='size-full'>
            <Image
              objectFit="cover"
              src={blockMoldure1Img}
              alt="block moldure image"
              style={{ position: 'relative',width: '80%', height: '80%', marginTop:'11vh', marginBottom:'11.2vh', left:'8vw' }}
            />
            <div className='max-w-[600px]'>
                <p className="text-black text-right text-2xl relative top-[-50vh] left-[23vh] font-bold">
                    A Inteligência Artificial é um campo da ciência da computação que busca desenvolver sistemas capazes de realizar tarefas que, tradicionalmente, demandam inteligência humana. <br/>
                    Isso inclui a capacidade de aprender com experiências passadas, resolver problemas,<br/> 
                    reconhecer padrões e interagir de forma adaptativa com o ambiente.
                </p>
            </div>
        </div>
    </div>
  );
};
