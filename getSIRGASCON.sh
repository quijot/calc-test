#!/bin/bash

#sem=(1640 1650 1660 1670 1680 1690 1700 1710 1720 1730 1740 1750 1760 1770 1780 1790 1800 1810 1820 1830 1840 1850 1860 1870 1880 1890 1900 1909)
sem=(1640 1641 1642 1643 1644 1645 1646 1647 1648 1649 1650 1651 1652 1653 1654 1655 1656 1657 1658 1659 1660 1661 1662 1663 1664 1665 1666 1667 1668 1669 1670 1671 1672 1673 1674 1675 1676 1677 1678 1679 1680 1681 1682 1683 1684 1685 1686 1687 1688 1689 1690 1691 1692 1693 1694 1695 1696 1697 1698 1699 1700 1701 1702 1703 1704 1705 1706 1707 1708 1709 1710 1711 1712 1713 1714 1715 1716 1717 1718 1719 1720 1721 1722 1723 1724 1725 1726 1727 1728 1729 1730 1731 1732 1733 1734 1735 1736 1737 1738 1739 1740 1741 1742 1743 1744 1745 1746 1747 1748 1749 1750 1751 1752 1753 1754 1755 1756 1757 1758 1759 1760 1761 1762 1763 1764 1765 1766 1767 1768 1769 1770 1771 1772 1773 1774 1775 1776 1777 1778 1779 1780 1781 1782 1783 1784 1785 1786 1787 1788 1789 1790 1791 1792 1793 1794 1795 1796 1797 1798 1799 1800 1801 1802 1803 1804 1805 1806 1807 1808 1809 1810 1811 1812 1813 1814 1815 1816 1817 1818 1819 1820 1821 1822 1823 1824 1825 1826 1827 1828 1829 1830 1831 1832 1833 1834 1835 1836 1837 1838 1839 1840 1841 1842 1843 1844 1845 1846 1847 1848 1849 1850 1851 1852 1853 1854 1855 1856 1857 1858 1859 1860 1861 1862 1863 1864 1865 1866 1867 1868 1869 1870 1871 1872 1873 1874 1875 1876 1877 1878 1879 1880 1881 1882 1883 1884 1885 1886 1887 1888 1889 1890 1891 1892 1893 1894 1895 1896 1897 1898 1899 1900 1901 1902 1903 1904 1905 1906 1907 1908 1909 1910 1911 1912 1913 1914 1915 1916 1917 1918 1919 1920)
eps=(ALUM AZUL BCAR CATA EBYP ESQU IGM1 LHCL LPGS MA01 MZAC RWSN SL01 SRLP TUCU UCOR UNRO UNSA UYTA VBCA CORD GUAY MPL2 NESA PEJO PRNA RECO UYPA UYSO UYTD)

# convertir coordenadas xyz -> lla
source convert.sh

sss=sss
sol=ibg
dir=desvios
output=$dir/__ALL.tsv

echo -e "ep\td_lat\td_lon\tfecha" > $output

for s in "${sem[@]}"
do
    :
    if [ ! -f $sss/$sol*P$s.crd ]; then
        cd $sss
        wget ftp://ftp.sirgas.org/pub/gps/SIRGAS/$s/$sol*P$s.crd
        cd ..
    fi
    for ep in "${eps[@]}"
    do
        :
        if [ ! -f $sss/$sol*P$s.crd ]; then
            ep_output=$dir/$ep.tsv
            ep=$(cat $sss/$sol*P$s.crd | grep $ep | awk '{ print $2 }')
            x=$(cat $sss/$sol*P$s.crd | grep $ep | awk '{ print $4 }')
            y=$(cat $sss/$sol*P$s.crd | grep $ep | awk '{ print $5 }')
            z=$(cat $sss/$sol*P$s.crd | grep $ep | awk '{ print $6 }')
            epoch=$(cat $sss/$sol*P$s.crd | grep EPOCH | awk '{ print $6 }')
            if [ ! -z ${x+x} ]; then
                if [ ! -f $ep_output ]; then
                    python correct.py $ep $x $y $z $epoch > $ep_output
                else
                    python correct.py $ep $x $y $z $epoch >> $ep_output
                fi
                python correct.py $ep $x $y $z $epoch >> $output
            fi
        fi
    done
done

python makecharts.py
python makeflow.py

