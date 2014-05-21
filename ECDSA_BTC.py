#! /usr/bin/env python
# coding=utf8

# ECDSA BTC of FastSignVerify
# Copyright (C) 2014  Antoine FERRON

# Some portions based on :
# "python-ecdsa" Copyright (C) 2010 Brian Warner (MIT Licence)
# "Simple Python elliptic curves and ECDSA" Copyright (C) 2005 Peter Pearson (public domain)
# "Electrum" Copyright (C) 2011 thomasv@gitorious (GPL)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>


# Signature is done with a random k
# from os.urandom

import os
from B58 import *
import binascii
import base64

class CurveFp( object ):
  def __init__( self, p, b ):
    self.__p = p
    self.__b = b

  def p( self ):
    return self.__p

  def b( self ):
    return self.__b

  def contains_point( self, x, y ):
    return ( y * y - ( x * x * x + self.__b ) ) % self.__p == 0

class Point( object ):
  def __init__( self, x, y, order = None ):
    self.__x = x
    self.__y = y
    self.__order = order

  def __eq__( self, other ):
    if self.__x == other.__x   \
     and self.__y == other.__y:
      return True
    else:
      return False

  def __add__( self, other ):
    if other == INFINITY: return self
    if self == INFINITY: return other
    p=curve_256.p()
    if self.__x == other.__x:
      if ( self.__y + other.__y ) % p == 0:
        return INFINITY
      else:
        return self.double()
    l = ( ( other.__y - self.__y ) * inverse_mod( other.__x - self.__x, p ) ) % p
    x3 = ( l * l - self.__x - other.__x ) % p
    y3 = ( l * ( self.__x - x3 ) - self.__y ) % p
    return Point( x3, y3 )

  def __mul__( self, other ):
    e = other
    if self.__order: e = e % self.__order
    if e == 0: return INFINITY
    if self == INFINITY: return INFINITY
    assert e > 0
    e3 = 3 * e
    negative_self = Point( self.__x, -self.__y, self.__order )
    i = 0x100000000000000000000000000000000000000000000000000000000000000000L
    while i > e3: i >>= 1L
    result = self
    while i > 2L:
      i >>= 1L
      result = result.double()
      ei = e&i
      if (e3&i)^ei : 
        if ei==0L    : result += self
        else         : result += negative_self
    return result

  def __rmul__( self, other ):
   return self * other

  def __str__( self ):
    if self == INFINITY: return "infinity"
    return "(%d,%d)" % ( self.__x, self.__y )

  def double( self ):
    p=curve_256.p()
    if self == INFINITY:
      return INFINITY
    xyd=((self.__x*self.__x)*inverse_mod(2*self.__y,p))%p
    x3=(9*xyd*xyd-2*self.__x)%p
    y3=(3*xyd*(self.__x-x3)-self.__y)%p
    return Point( x3, y3 )

  def x( self ):
    return self.__x

  def y( self ):
    return self.__y

  def curve( self ):
    return self.__curve
  
  def order( self ):
    return self.__order
    
INFINITY = Point( None, None )

def inverse_mod( a, m ):
  if a < 0 or m <= a: a = a % m
  c, d = a, m
  uc, vc, ud, vd = 1, 0, 0, 1
  while c != 0:
    q, c, d = divmod( d, c ) + ( c, )
    uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
  assert d == 1
  if ud > 0: return ud
  else: return ud + m

# secp256k1
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2FL
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
_b = 0x0000000000000000000000000000000000000000000000000000000000000007L
#a = 0x00
_Gx= 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798L
_Gy= 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8L

def dsha256(message):
  if type(message) is unicode: message=message.encode('utf-8')
  hash1=hashlib.sha256(message).digest()
  return int(hashlib.sha256(hash1).hexdigest(),16)

class Signature( object ):
  def __init__( self, pby, r, s ):
    self.r = r
    self.s = s
    self.pby = pby

  def encode(self):
    sigr = binascii.unhexlify(("%064x" % self.r).encode())
    sigs = binascii.unhexlify(("%064x" % self.s).encode())
    return sigr+sigs

class Public_key( object ):
  def __init__( self, generator, point ):
    self.generator = generator
    self.point = point
    n = generator.order()
    if not n:
      raise RuntimeError, "Generator point must have order."
    if not n * point == INFINITY:
      raise RuntimeError, "Generator point order is bad."
    if point.x() < 0 or n <= point.x() or point.y() < 0 or n <= point.y():
      raise RuntimeError, "Generator point has x or y out of range."

  def verifies( self, msg_aver, signature ):
    if self.point == INFINITY: return False
    G = self.generator
    n = G.order()
    #if self.point.x() < 0 or n <= self.point.x() or self.point.y() < 0 or n <= self.point.y(): return False
    if not curve_256.contains_point(self.point.x(),self.point.y()): return False
    #if n * self.point != INFINITY: return False
    hash=msg_aver
    r = signature.r
    s = signature.s
    if r < 1 or r > n-1: return False
    if s < 1 or s > n-1: return False
    c = inverse_mod( s, n )
    u1 = ( hash * c ) % n
    u2 = ( r * c ) % n
    xy = u1 * G + u2 * self.point
    v = xy.x() % n
    return v == r

class Private_key( object ):
  def __init__( self, public_key, secret_multiplier ):
    self.public_key = public_key
    self.secret_multiplier = secret_multiplier

  def der( self ):
    hex_der_key = '06052b8104000a30740201010420' + \
                  '%064x' % self.secret_multiplier + \
                  'a00706052b8104000aa14403420004' + \
                  '%064x' % self.public_key.point.x() + \
                  '%064x' % self.public_key.point.y()
    return hex_der_key.decode('hex')

  def sign( self, msg_asig, k ):
    hash=dsha256(msg_asig)
    G = self.public_key.generator
    n = G.order()
    p1 = k * G
    r = p1.x()
    pby= p1.y()&1
    if r == 0: raise RuntimeError, "amazingly unlucky random number r"
    s = ( inverse_mod( k, n ) * ( hash + ( self.secret_multiplier * r ) % n ) ) % n
    if s == 0: raise RuntimeError, "amazingly unlucky random number s"
    return Signature( pby, r, s )

def randoml(pointgen):
  cand = 0
  while cand<1 or cand>=pointgen.order():
    cand=int(os.urandom(32).encode('hex'), 16)
  return cand

def is_address(addr):
    ADDRESS_RE = re.compile('[1-9A-HJ-NP-Za-km-z]{26,}\\Z')
    if not ADDRESS_RE.match(addr): return False
    try:
        addrtype, h = bc_address_to_hash_160(addr)
    except Exception:
        return False
    return addr == hash_160_to_bc_address(h, addrtype)

def bitcoin_sign_message(privkey, message, k):
  return privkey.sign( "\x18Bitcoin Signed Message:\n" \
                       + chr(len(message)) + message  , 
                       k )

def bitcoin_encode_sig(signature):
  return chr( 27 + signature.pby ) + signature.encode()

def output_full_sig(text,address,signature):
    fullsig= \
    "-----BEGIN BITCOIN SIGNED MESSAGE-----\n" \
    +text+ "\n" + \
    "-----BEGIN SIGNATURE-----\n" \
    +address+ "\n" +  \
    signature+ "\n" + \
    "-----END BITCOIN SIGNED MESSAGE-----"
    return fullsig
    

def bitcoin_verify_message(address, signature, message):
        G = generator_256
        order = G.order()
        # extract r,s from signature
        sig = base64.b64decode(signature)
        if len(sig) != 65: raise Exception("Wrong encoding")
        r = int(binascii.hexlify(sig[ 1:33]),16)
        s = int(binascii.hexlify(sig[33:  ]),16)
        nV = ord(sig[0])
        if nV < 27 or nV >= 35:
            raise Exception("Bad encoding")
        if nV >= 31:
            compressed = True
            raise Exception("Compressed signature not yet managed")
            nV -= 4
        else:
            compressed = False
        recid = nV - 27
        p=curve_256.p()
        xcube= pow(r,3,p)
        exposa=(p+1)>>2
        beta = pow(xcube+7, exposa, p)
        if (beta - recid) % 2 == 0:
            y = beta
        else:
            y = p - beta
        R = Point(r, y, order)
        # check R is on curve
        assert curve_256.contains_point(r,y)
        # checks that nR is at infinity
        assert order*R==INFINITY
        e = dsha256( "\x18Bitcoin Signed Message:\n" \
                       + chr(len(message)) + message )
        minus_e = -e % order
        # Q = r^-1 (sR - eG)
        inv_r = inverse_mod(r,order)
        Q = inv_r * ( s * R + minus_e * G )
        # checks Q in range, Q on curve, Q order
        pubkey = Public_key( G, Q)
        # checks that Q is the public key of the signature
        assert pubkey.verifies( e, Signature(0,r,s) )
        # checks th eaddress provided is the signing address
        addr = pub_hex_base58( pubkey.point.x(), pubkey.point.y() )
        if address != addr:
            raise Exception("Bad signature")

curve_256 = CurveFp( _p, _b )
generator_256 = Point( _Gx, _Gy, _r )