import React from 'react'
import {motion} from 'framer-motion'

export default function Box4() {
    const boxVariant = {
        hidden:{
            x: "-100vw"
        },
        visible:{
            x:0,
            transition:{
                delay: 0.3,
                when: "beforeChildren"

            }

        }

    }
    const listVariant = {
        hidden:{
            x: "-10",
            opacity: 0
        },
        visible:{
            x:0,
            opacity: 1,
            transition:{
                delay: 1,
                staggerChildren: 0.2

            }

        }

    }
    
  return (
    <div className='box-container'>
        <motion.div className='box'
        variants={boxVariant}
        animate="visible"
        initial="hidden">
         {[1,2,3].map(box => {
            return <motion.li className='box-item'
            variants={listVariant}

            ></motion.li>
         })}
        </motion.div>
      
    </div>
  )
}
