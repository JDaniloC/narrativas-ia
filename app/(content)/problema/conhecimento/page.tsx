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
    <div className={`${openSans.className} flex lg:size-full flex-col-reverse lg:flex-row`}>
        <div className="text-white text-xl gap-10 p-10 flex flex-col lg:mt-20 w-full lg:w-2/5">
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
        <div className='right-0 size-full lg:w-2/3 p-10 relative'>
            <div className='size-full'>
              <Image
                objectFit="cover"
                src={blockMoldure1Img}
                alt="block moldure image"
                style={{ marginLeft: 'auto' }}
              />
            </div>
            <p className="text-black text-right absolute w-4/5 right-10 font-bold p-10 top-[10vw] 2xl:top-1/3 text-md md:text-2xl">
              A Inteligência Artificial é um campo da ciência da computação que busca desenvolver sistemas capazes de realizar tarefas que, tradicionalmente, demandam inteligência humana. <br/>
              Isso inclui a capacidade de aprender com experiências passadas, resolver problemas, reconhecer padrões e interagir de forma adaptativa com o ambiente.
            </p>
        </div>
    </div>
  );
};
