"""


:mod:`Initializators` -- initialization methods module
===================================================================

In this module we have the genetic operators of initialization for each
chromosome representation, the most part of initialization is done by
choosing random data.

.. note:: In Pyevolve, the Initializator defines the data type that will
          be used on the chromosome, for example, the :func:`G1DListInitializatorInteger`
          will initialize the G1DList with Integers.
          

"""

from random import randint as rand_randint, uniform as rand_uniform, choice as rand_choice
import GTree
import Util
from _ast import Num
import copy

#############################
##     1D Binary String    ##
#############################


def G1DBinaryStringInitializator(genome, **args):
   """ 1D Binary String initializator """
   genome.genomeList = [ rand_choice((0,1)) for i in xrange(genome.getListSize()) ]

#############################
##     2D Binary String    ##
#############################

def G2DBinaryStringInitializator(genome, **args):
   """ Integer initialization function of 2D Binary String
   
   .. versionadded:: 0.6
      The *G2DBinaryStringInitializator* function
   """
   genome.clearString()
   
   for i in xrange(genome.getHeight()):
      for j in xrange(genome.getWidth()):
         random_gene = rand_choice((0,1))
         genome.setItem(i, j, random_gene)


####################
##     1D List    ##
####################

#####
def G1DListInitializatorInteger_my(genome, **args):
    a=genome.My_get_listdic()
    list_dic=copy.deepcopy(a[0])
    list_margin=copy.deepcopy(a[1])
    totalmoney=a[2]
    list_zhonglei=a[3]
    all_money=totalmoney
    num=genome.getListSize()
    g_list=[0]*num
    first_lic=['CU','IF','RU']
    second_lic=['I','M','RB','SR','TA','Y']
    ''''IF':90000,'CU':30000,'RU':10000,'I':3500,'M':1500,'RB':1500,'SR':3000,'TA':2000,'Y':3500'''
    while(1):
            if all_money<totalmoney*0.4 or all_money<10000:
                break
            len_cu=len(list_dic['CU'])
            len_if=len(list_dic['IF'])
            len_ru=len(list_dic['RU'])
            if len_cu<=0 and len_if<=0 and len_ru<=0:
                break
            for i in first_lic:
                len_dic=len(list_dic[i])
                if len_dic<=0:
                    continue
                if all_money>list_margin[i]:
                    if len_dic>1:
                        j=rand_randint(0,len_dic-1)
                    else:
                        j=0
                    money=list_margin[i]
                    all_lot=int(all_money/money)
                    lot=rand_randint(0,all_lot)
                    all_money=all_money-money*lot
                    n=list_dic[i][j]
                    g_list[n]=lot
                    del list_dic[i][j]
    while(1):
            if  all_money<2000:
                break
            sum=0
            for i in second_lic:
                sum=sum+len(list_dic[i])
            if sum<=0:
                break
            for i in second_lic:
                len_dic=len(list_dic[i])
                if len_dic<=0:
                    continue
                if all_money>list_margin[i]:
                    if len_dic>1:
                        j=rand_randint(0,len_dic-1)
                    else:
                        j=0
                    money=list_margin[i]
                    all_lot=int(all_money/money)
                    lot=rand_randint(0,all_lot)
                    all_money=all_money-money*lot
                    n=list_dic[i][j]
                    g_list[n]=lot
                    del list_dic[i][j]
            sum_l=0
            for i in second_lic:
                sum_l=sum_l+len(list_dic[i])
            if sum==sum_l:
                break
    #print g_list
    genome.genomeList=g_list
   


def G1DListInitializatorAllele(genome, **args):
   """ Allele initialization function of G1DList

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   """

   allele = genome.getParam("allele", None)
   if allele is None:
      Util.raiseException("to use the G1DListInitializatorAllele, you must specify the 'allele' parameter")

   genome.genomeList = [ allele[i].getRandomAllele() for i in xrange(genome.getListSize())  ]

def G1DListInitializatorInteger(genome, **args):
    
   """ Integer initialization function of G1DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   """
   r=genome.getParam("range_list", None)
   
   if r is None:
      
      range_min = genome.getParam("rangemin", 0)
      range_max = genome.getParam("rangemax", 100)

      genome.genomeList = [rand_randint(range_min, range_max) for i in xrange(genome.getListSize())]
   else:

      genome.genomeList = [rand_randint(0, r[i]) for i in xrange(genome.getListSize())]
def G1DListInitializatorReal(genome, **args):
	
	
   """ Real initialization function of G1DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   """
   length=genome.getParam("length", 2)
   r=genome.getParam("range_list", None)
   
   if r is None:
      
      range_min = genome.getParam("rangemin", 0)
      range_max = genome.getParam("rangemax", 100)

      genome.genomeList = [round(rand_uniform(range_min, range_max),length) for i in xrange(genome.getListSize())]
   else:

      genome.genomeList = [round(rand_uniform(r[i][0], r[i][1]),length) for i in xrange(genome.getListSize())]
   




####################
##     2D List    ##
####################
def G2DListInitializatorInteger(genome, **args):
   """ Integer initialization function of G2DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.
   
   """
   genome.clearList()

   for i in xrange(genome.getHeight()):
      for j in xrange(genome.getWidth()):
         randomInteger = rand_randint(genome.getParam("rangemin", 0),
                                      genome.getParam("rangemax", 100))
         genome.setItem(i, j, randomInteger)


def G2DListInitializatorReal(genome, **args):
   """ Integer initialization function of G2DList

   This initializator accepts the *rangemin* and *rangemax* genome parameters.

   """
   genome.clearList()
   
   for i in xrange(genome.getHeight()):
      for j in xrange(genome.getWidth()):
         randomReal = rand_uniform(genome.getParam("rangemin", 0),
                                   genome.getParam("rangemax", 100))
         genome.setItem(i, j, randomReal)

def G2DListInitializatorAllele(genome, **args):
   """ Allele initialization function of G2DList

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   .. warning:: the :class:`GAllele.GAlleles` instance must have the homogeneous flag enabled

   """

   allele = genome.getParam("allele", None)
   if allele is None:
      Util.raiseException("to use the G2DListInitializatorAllele, you must specify the 'allele' parameter")

   if allele.homogeneous == False:
      Util.raiseException("to use the G2DListInitializatorAllele, the 'allele' must be homogeneous")

   genome.clearList()
   
   for i in xrange(genome.getHeight()):
      for j in xrange(genome.getWidth()):
         random_allele = allele[0].getRandomAllele()
         genome.setItem(i, j, random_allele)

####################
##      Tree      ##
####################

def GTreeInitializatorInteger(genome, **args):
   """ Integer initialization function of GTree

   This initializator accepts the *rangemin* and *rangemax* genome parameters.
   It accepts the following parameters too:
      
   *max_depth*
      The max depth of the tree

   *max_siblings*
      The number of maximum siblings of an node

   *method*
      The method, accepts "grow", "full" or "ramped".

   .. versionadded:: 0.6
      The *GTreeInitializatorInteger* function.
   """
   max_depth = genome.getParam("max_depth", 5)
   max_siblings = genome.getParam("max_siblings", 2)

   range_min = genome.getParam("rangemin", 0)
   range_max = genome.getParam("rangemax", 100)

   lambda_generator = lambda: rand_randint(range_min, range_max)

   method = genome.getParam("method", "grow")

   if method == "grow":
      root = GTree.buildGTreeGrow(0, lambda_generator, max_siblings, max_depth)
   elif method == "full":
      root = GTree.buildGTreeFull(0, lambda_generator, max_siblings, max_depth)
   elif method == "ramped":
      if Util.randomFlipCoin(0.5):
         root = GTree.buildGTreeGrow(0, lambda_generator, max_siblings, max_depth)
      else:
         root = GTree.buildGTreeFull(0, lambda_generator, max_siblings, max_depth)
   else:
      Util.raiseException("Unknown tree initialization method [%s] !" % method)

   genome.setRoot(root)
   genome.processNodes()
   assert genome.getHeight() <= max_depth

def GTreeInitializatorAllele(genome, **args):
   """ Allele initialization function of GTree

   To use this initializator, you must specify the *allele* genome parameter with the
   :class:`GAllele.GAlleles` instance.

   .. warning:: the :class:`GAllele.GAlleles` instance **must** have the homogeneous flag enabled

   .. versionadded:: 0.6
      The *GTreeInitializatorAllele* function.
   """
   max_depth    = genome.getParam("max_depth", 5)
   max_siblings = genome.getParam("max_siblings", 2)
   method       = genome.getParam("method", "grow")

   allele = genome.getParam("allele", None)
   if allele is None:
      Util.raiseException("to use the GTreeInitializatorAllele, you must specify the 'allele' parameter")

   if allele.homogeneous == False:
      Util.raiseException("to use the GTreeInitializatorAllele, the 'allele' must be homogeneous")

   if method == "grow":
      root = GTree.buildGTreeGrow(0, allele[0].getRandomAllele, max_siblings, max_depth)
   elif method == "full":
      root = GTree.buildGTreeFull(0, allele[0].getRandomAllele, max_siblings, max_depth)
   elif method == "ramped":
      if Util.randomFlipCoin(0.5):
         root = GTree.buildGTreeGrow(0, allele[0].getRandomAllele, max_siblings, max_depth)
      else:
         root = GTree.buildGTreeFull(0, allele[0].getRandomAllele, max_siblings, max_depth)
   else:
      Util.raiseException("Unknown tree initialization method [%s] !" % method)


   genome.setRoot(root)
   genome.processNodes()
   assert genome.getHeight() <= max_depth

####################
##      Tree GP   ##
####################

def GTreeGPInitializator(genome, **args):
   """This initializator accepts the follow parameters:
      
   *max_depth*
      The max depth of the tree

   *method*
      The method, accepts "grow", "full" or "ramped"

   .. versionadded:: 0.6
      The *GTreeGPInitializator* function.
   """

   max_depth = genome.getParam("max_depth", 5)
   method    = genome.getParam("method", "grow")
   ga_engine = args["ga_engine"]

   if method == "grow":
      root = GTree.buildGTreeGPGrow(ga_engine, 0, max_depth)
   elif method == "full":
      root = GTree.buildGTreeGPFull(ga_engine, 0, max_depth)
   elif method == "ramped":
      if Util.randomFlipCoin(0.5):
         root = GTree.buildGTreeGPFull(ga_engine, 0, max_depth)
      else:
         root = GTree.buildGTreeGPGrow(ga_engine, 0, max_depth)
   else:
      Util.raiseException("Unknown tree initialization method [%s] !" % method)

   genome.setRoot(root)
   genome.processNodes()
   assert genome.getHeight() <= max_depth
