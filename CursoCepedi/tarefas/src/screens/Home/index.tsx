import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export function Home() {
    return (
      <View style={styles.container}>
        <Text style={styles.label}>Login</Text>
        <TextInput
          style={styles.input}
          placeholder='Digite seu login'
        />
        <Text style={styles.label}>Senha</Text>
        <TextInput
          style={styles.input}
          placeholder='Digite sua senha'
          secureTextEntry
        />
        <StatusBar style="auto" />
        <TouchableOpacity style={styles.button}>
          <Text style={styles.textButton}>Login</Text>
        </TouchableOpacity>
        <View style={styles.separator} />
      </View>
    );
  }
  
  const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#141325',
      alignItems: 'center',
      justifyContent: 'center',
      padding: 16,
      gap: 16,
    },
    button: {
      backgroundColor: 'blue',
      padding: 10,
      // marginTop: 20,
      borderRadius: 16,
      width: "100%",
      alignItems: "center",
      borderColor: "#000",
      borderWidth: 1,
    },
    text: {
      color: 'white',
    },
    input: {
      backgroundColor: '#adadad',
      width: '100%',
      padding: 10,
      // marginTop: 20,
      marginHorizontal: 16,
      height: 56,
      borderRadius: 16,
    },
    label: {
      alignSelf: "flex-start",
      fontSize: 18,
    },
    textButton:{
      fontWeight: "700",
      textTransform: "uppercase"
    },
    separator:{
      marginTop:16,
      backgroundColor: "#FFF",
      height: 2,
      width: "80%",
    }
});
