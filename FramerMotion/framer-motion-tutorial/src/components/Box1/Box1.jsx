import React, { useState } from 'react'
import {motion} from 'framer-motion'

export default function Box1() {
  const [animating ,setIsAnimating ] = useState(false)
  return (
    <div className='box-container'>
        <motion.div 
        className='box'
        style ={{opacity: 0.2}}
        animate ={{
            x: animating?"100rem" : "0rem",
            opacity: animating?1 : 0.5,
            rotate: animating?360 : 0
        }}
        initial={{
            opacity: 0.1
        }}
        transition={{
          type:"spring",
          stiffness: 50,
          
        }}
        onClick={() => setIsAnimating(!animating)}
        >Click Me

        </motion.div>
      
    </div>
  )
}
