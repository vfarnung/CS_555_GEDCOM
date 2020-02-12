{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "File = open('Khalid_GEDCOM.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "New_file = open(\"Gedcome_khalid_project02.txt\",\"w\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "Lines = File.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "L1_tags = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHILL','DIV']\n",
    "L0_tags_1 =['INDI','FAM']\n",
    "L0_tags_2 =['HEAD','TRLR','NOTE']\n",
    "L2_tags =['DATE']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in Lines:  \n",
    "#print (line)\n",
    "\n",
    "    line = line.strip()\n",
    "    New_file.write(\"-->{}\".format(line))\n",
    "    New_file.write('\\n')\n",
    "    line = line.split(\" \")\n",
    "    #print (line)\n",
    "    level = line[0]\n",
    "    #print (level)\n",
    "    tags = line[1]\n",
    "    #print (tags)\n",
    "    arguments =line[2:]   \n",
    "    #print (arguments)\n",
    "    arg_ = \" \".join(arguments) \n",
    "\n",
    "    if level == '1':\n",
    "        if tags in L1_tags: \n",
    "            new = 'Y' \n",
    "            New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            New_file.write('\\n')\n",
    "        else:\n",
    "            new ='N'\n",
    "            New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            New_file.write('\\n')\n",
    "            \n",
    "    if level == '2':\n",
    "        if tags in L2_tags: \n",
    "            new = 'Y' \n",
    "            New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            New_file.write('\\n')\n",
    "        else:\n",
    "            new ='N'\n",
    "            New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            New_file.write('\\n')\n",
    "    if level == '3':\n",
    "        new = 'N' \n",
    "        New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "        New_file.write('\\n')\n",
    "    if level =='0':\n",
    "        \n",
    "        if arg_ in L0_tags_1: \n",
    "            new ='Y'\n",
    "            New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(arguments) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(tags)+'\\n') \n",
    "            New_file.write('\\n')\n",
    "        else:\n",
    "            if tags in L0_tags_2:            \n",
    "                new = 'Y' \n",
    "                New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "                New_file.write('\\n')\n",
    "            else:\n",
    "                new = 'N' \n",
    "                New_file.write(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "                New_file.write('\\n')\n",
    "New_file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for line in Lines:  \n",
    "#print (line)\n",
    "\n",
    "    line = line.strip()\n",
    "    print(\"-->{}\".format(line))\n",
    "    #New_file.write('\\n')\n",
    "    line = line.split(\" \")\n",
    "    #print (line)\n",
    "    level = line[0]\n",
    "    #print (level)\n",
    "    tags = line[1]\n",
    "    #print (tags)\n",
    "    arguments =line[2:]   \n",
    "    #print (arguments)\n",
    "    arg_ = \" \".join(arguments) \n",
    "\n",
    "    if level == '1':\n",
    "        if tags in L1_tags: \n",
    "            new = 'Y' \n",
    "            print (\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            #New_file.write('\\n')\n",
    "            \n",
    "    if level == '2':\n",
    "        if tags in L2_tags: \n",
    "            new = 'Y' \n",
    "            print(\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            #New_file.write('\\n')\n",
    "    else:\n",
    "        new ='N'\n",
    "        print (\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "            #New_file.write('\\n')\n",
    "    if level == '0':\n",
    "        if arg_ in L0_tags_1: \n",
    "            new ='Y'\n",
    "            print (\"<--\"+ \"\".join(level) + \"|\" + \"\".join(arguments) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(tags)+'\\n') \n",
    "            #New_file.write('\\n')\n",
    "        else:\n",
    "            if tags in L0_tags_2:            \n",
    "                new = 'Y' \n",
    "                print (\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "                #New_file.write('\\n')\n",
    "            else:\n",
    "                new = 'N' \n",
    "                print (\"<--\"+ \"\".join(level) + \"|\" + \"\".join(tags) + \"|\" +\"\".join(new)+ \"|\" + \"\".join(arguments)+'\\n')\n",
    "                #New_file.write('\\n')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}