import React from 'react';
import Image from 'next/image';
import { blockMoldure2Img } from '../problema-images';
import { Open_Sans } from 'next/font/google';

const openSans = Open_Sans({
  subsets: ['latin'],
  variable: '--open-sans',
})

export default function AIUsePage() {
  return (
    <div className={`${openSans.className} flex w-full flex-col-reverse lg:flex-row-reverse bg-[#83F0FF]`}>
        <div className="text-black text-xl gap-10 p-10 flex flex-col lg:mt-10 w-full lg:w-2/5">
            <p>
                Algoritmos de IA também desempenham um papel vital na segurança digital, identificando padrões incomuns que podem indicar atividades fraudulentas. Isso é crucial para a proteção dos usuários em transações financeiras online e na prevenção de ataques cibernéticos.Andrew Ng, um destacado cientista da computação e defensor da inteligência artificial, ressalta que esses avanços não apenas melhoram a eficiência dos sistemas, mas também contribuem para a segurança e conveniência dos usuários, promovendo uma experiência digital mais fluida e segura.
            </p>
            <p className="text-xl text-right">
                No entanto, a coleta extensiva de dados pode resultar em violações de privacidade, especialmente quando as medidas de segurança não são suficientes. Vazamentos de informações pessoais são uma ameaça constante, expondo usuários a riscos de roubo de identidade e outros crimes cibernéticos.
                <br />
                <br />
                Algoritmos de IA podem herdar e amplificar os preconceitos presentes nos dados de treinamento, resultando em discriminação injusta, exacerbando disparidades sociais e prejudicando grupos minoritários. A falta de transparência dos algoritmos levanta questões sobre a compreensão e o controle que os usuários têm sobre o uso de seus dados. A ausência de transparência pode minar a confiança do público e criar um ambiente onde as decisões automatizadas não são compreendidas.
            </p>
            <p>
                A Inteligência Artificial é como ensinamos computadores a pensar e aprender como seres humanos. É uma tecnologia que ajuda as máquinas a entenderem coisas. Mas, assim como tem pontos positivos, também pode ter desafios, como quando queremos manter nossas informações privadas, evitar decisões injustas ou entender como os computadores tomam decisões.
            </p>
        </div>
        <div className='size-full lg:w-3/5 p-10 relative'>
            <div className='size-full'>
              <Image
                objectFit="cover"
                src={blockMoldure2Img}
                alt="block moldure image"
                style={{ marginLeft: 'auto' }}
              />
            </div>
            <p className="text-white absolute w-4/5 left-10 font-bold p-10 top-[10vw] 2xl:top-1/3 text-md md:text-2xl">
              Um dos pontos mais destacados é a capacidade da IA de personalizar serviços com base na análise de dados. Plataformas de streaming, por exemplo, utilizam algoritmos para entender os gostos dos usuários, oferecendo recomendações de filmes e séries. Isso não apenas aprimora a experiência do usuário, mas também impulsiona a fidelidade à plataforma.
            </p>
        </div>
    </div>
  );
};
