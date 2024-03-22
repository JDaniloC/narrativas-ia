import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { moldure, title, arrow } from './problema-images'
import { pixterDisplay } from '@/fonts';

export default function ProblemaIndexPage() {
  return (
    <div className={`${pixterDisplay.className} flex flex-col justify-center items-center`}>
      <div className='max-h-full max-w-full relative'>
        <div className='size-full'>
          <Image
            src={moldure}
            alt="page moldure"
            objectFit="cover"
          />
        </div>
        <div className='size-full absolute top-0 z-10'>
          <p className='text-[#83F0FF] text-3xl md:text-6xl lg:text-7xl xl:text-8xl relative top-4 md:top-8 lg:top-12 left-4 md:left-8'>
            {'//: A PROBLEMÁTICA DA IA'}
          </p>
          <div className='flex flex-col md:flex-row relative left-4 md:left-8 top-12 md:top-28 w-full gap-4 md:gap-10'>
            <div className='relative h-40 md:h-96 lg:h-80 w-full md:w-3/5 lg:w-[50%]'>
              <Image
                src={title}
                alt="page title"
                layout="fill"
                objectFit="cover"
              />
            </div>
            <p className='text-[#83F0FF] text-xl md:text-3xl lg:text-4xl mt-4 md:mt-0'>
              {'//:TÓPICOS'}
            </p>
            <div className='w-full md:w-[45%] lg:w-60 xl:w-80 mt-2 md:mt-0'>
              <hr className="h-px border-[1px] border-[#83F0FF]"/>
              <Link href="/problema/page1">
                <Button variant="ghost" className='p-0 m-0 w-full flex justify-start py-4 md:py-10'>
                  <p className='text-[#83F0FF] text-lg md:text-xl lg:text-2xl xl:text-3xl'>
                    {'//:001'}
                  </p>
                  <p className='ml-4 md:ml-8 mr-auto font-sans text-base md:text-lg lg:text-xl xl:text-2xl'>
                    Você conhece alguma IA?
                  </p>
                  <Image
                    src={arrow}
                    alt="Seta"
                    width={20}
                    height={20}
                  />
                </Button>
              </Link>
              <hr className="h-px border-[1px] border-[#83F0FF]"/>
              <Link href="/problema/page2">
                <Button variant="ghost" className='p-0 m-0 w-full flex justify-start py-4 md:py-10'>
                  <p className='text-[#83F0FF] text-lg md:text-xl lg:text-2xl xl:text-3xl'>
                    {'//:002'}
                  </p>
                  <p className='ml-4 md:ml-8 mr-auto font-sans text-base md:text-lg lg:text-xl xl:text-2xl'>
                    IA no dia a dia
                  </p>
                  <Image
                    src={arrow}
                    alt="Seta"
                    width={20}
                    height={20}
                  />
                </Button>
              </Link>
              <hr className="h-px border-[1px] border-[#83F0FF]"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
