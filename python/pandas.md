# DataFrame
## Create from ndarray
```
>>> nda = np.ndarray(shape=(2,2), dtype=float)
>>> nda
array([[  0.00000000e+000,   3.24370112e+178],
       [  4.66096380e-309,   2.50521680e-292]])
>>> dfa = pd.DataFrame(nda)  # it creates default columns and indexes
>>> dfa
               0              1
0   0.000000e+00  3.243701e+178
1  4.660964e-309  2.505217e-292

>>> dfa = pd.DataFrame(nda, columns=('col1', 'col2'))
>>> dfa
            col1           col2
0   0.000000e+00  3.243701e+178
1  4.660964e-309  2.505217e-292
>>> dfa = pd.DataFrame(nda, columns=('col1', 'col2'), index=['row1', 'row2'])
>>> dfa
               col1           col2
row1   0.000000e+00  3.243701e+178
row2  4.660964e-309  2.505217e-292

# dataframe is column first, but ndarray is row first.
>>> dfa['col1']['row2']
4.6609637972718334e-309
>>> nda[0][0]
0.0
>>> nda[1][0]
4.6609637972718334e-309
```
## Plot
```python
arr = { 'm_srcaddr':['10.19.139.141', '10.19.139.142', '10.19.139.143', '10.19.139.144', '10.19.139.145'], 'total_fwd_size': [2479.335,888.141, 1111, 2222, 3555]}
df = pd.DataFrame(arr)
type(df['m_srcaddr'][0])
df.plot(x = 'm_srcaddr')
plt.xticks(df.index, df['m_srcaddr'], rotation=90)
plt.show()
```
